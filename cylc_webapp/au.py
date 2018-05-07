'''
    FILE: au.py
    PURPOSE: establish secure connection to cylc running instance
    PRECONDITIONS: A running instance of CYLC, the hostname, port number, passphrase,
    and certificate of the suite. Iorder to view these simply check your "concat"
    file within your suite folder. Might be something like cylc-run/my.suite/.services
'''
import requests
import json
import os
from anytree import Node, RenderTree
from job import Job, JobNode
from port import getPorts
from anytree import Node, RenderTree

SUITE = "my.suite"
HOST_NAME = 'bigbrotherx52-cylc-capstone-sp18-5942931'
PORT_LIST = getPorts(HOST_NAME)
newpath = r'cylc_webapp/cylc-variables' 


'''
    Returns the passphrase as read from the file saved in the '.service/passphrase'
    @param {str} suite, the name of the suite 
    TODO: dynamically retrieve passphrase file, error check path, os build path rather than concat
'''
def getPassphrase(suite):
    # if not os.path.exists(newpath):
    #     os.makedirs(newpath)
    # passphraseFile = "/home/ubuntu/workspace/cylc_webapp/cylc-variables/"+ SUITE +"/passphrase"
    
    passphrase_file = "/home/ubuntu/cylc-run/" + suite + "/.service/passphrase"
    with open(passphrase_file,'r') as f:
       	passphrase = f.readline()
    return passphrase

'''
    Returns a dictionary of string keys and Job Array values
    @param {[Job]} jobs, A list of Jobs
'''  
def getCycleHierarchy(jobs):
    cycle_hierarchy = {}
    for job in jobs:
        if cycle_hierarchy.has_key(job.label):
            cycle_hierarchy[job.label].append(job)
        else:
            cycle_hierarchy[job.label] = [job]
    return cycle_hierarchy
            

'''
    Returns a dictionary with string keys and JobNode values (trees)
    @param {JSON} suite_json, The returned JSON from the request to 'get_latest_state'
    @param {dict} cycles The, cycle hierarchy for the jobs
'''
def getFamilyHierarchy(suite_json, cycles):
    ancestors = suite_json["ancestors_pruned"]
    cycle_vals = {}
    groupings = {}
    for cycle, jobs in sorted(cycles.items()):
      # add a root cycle node to the dictionary 
      cycle_vals[cycle] = JobNode(cycle, Job(**{'label' : cycle, 'is_group' : True}))
      
      # iterate through this cycle's jobs
      for job in jobs:
        # these values reset for each job
        order = ancestors[job.name]
        root = cycle_vals[cycle]
        parent_id = root.id
        
        # if the job has a family grouping / parent 
        if (len(order) > 2):
          
          # iterate through its family in reverse (excluding first and last)
          for element in reversed(order[1:-1]):
            # for unique ids we need the name and it's parent's name 
            group_id = element + parent_id
            
            # create a new grouping if it doesn't already exist
            if group_id not in groupings:
              groupings[group_id] = JobNode(group_id, Job(**{'is_group' : True}), parent = root)
              
            # connect only if last item
            if (element == order[1]):
              JobNode(job.name + job.label, job, parent = groupings[group_id])
            
            # update parent for the next one
            root = groupings[group_id]
            parent_id = root.id
              
        # otherwise job just goes under root cycle node
        else:
          JobNode(job.name + job.label, job, parent = root)
          
    return cycle_vals
'''
    Returns an array of Job objects
    @param {JSON} suite_json, The returned JSON from the request to 'get_latest_state'
'''
def parseJobs(suite_json):
    jobs = []
    index = 0
    for job, job_dict in suite_json["summary"][1].items():
        jobs.append( Job(**job_dict) )
        index += 1
    return jobs

'''
    Returns the path to the signed server certificate
    @param {str} suite, the name of the suite 
    @param {str} [path = None], the base path to the certificate 
    TODO: dynamically retrieve passphrase file, error check path, os build path rather than concat
'''
def getVerify(suite, path=None):
    # return "/home/ubuntu/workspace/cylc_webapp/cylc-variables/"+suite+"/ssl.cert"
    return "/home/ubuntu/cylc-run/" + suite + "/.service/ssl.cert"
    # need to make it so that the user can add the ssl & passphrase to a suite folder.

'''
    Returns an array of Job objects and a dictionary of strings, JobNodes as a tuple
    TODO: seperate API call from actual parsing of returned value
'''
def getResponse():
    auth = requests.auth.HTTPDigestAuth('cylc', getPassphrase(SUITE))
    session = requests.Session()
    for portNumber in PORT_LIST:
        url = "https://%s:%d/get_latest_state" % (HOST_NAME, portNumber)
        try:
            ret = session.get(
                                url,
                                auth = auth,
                                verify = getVerify(SUITE)
                             )
        
            response = ret.json()
            jobs = parseJobs(response)
            cycles = getCycleHierarchy(jobs)
            hierarchy = getFamilyHierarchy(response, cycles)
            
            for cycle_key, cycle_node in hierarchy.items():
              for pre, fill, node in RenderTree(cycle_node):
                print("%s%s" % (pre, node.id))
                
            print "TYPE:", type(hierarchy)
            
            return jobs, hierarchy
        except Exception, err: 
            print err
            
# getResponse()