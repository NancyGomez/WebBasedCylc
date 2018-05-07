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

def getPassphrase(suite):
    # TODO: make dynamic and error check path and os build path rather than concat
    
    # if not os.path.exists(newpath):
    #     os.makedirs(newpath)
    # passphraseFile = "/home/ubuntu/workspace/cylc_webapp/cylc-variables/"+ SUITE +"/passphrase"
    
    passphrase_file = "/home/ubuntu/cylc-run/" + suite + "/.service/passphrase"
    with open(passphrase_file,'r') as f:
       	passphrase = f.readline()
    return passphrase
    
def getCycleHierarchy(jobs):
    cycle_hierarchy = {}
    for job in jobs:
        if cycle_hierarchy.has_key(job.label):
            cycle_hierarchy[job.label].append(job)
        else:
            cycle_hierarchy[job.label] = [job]
    return cycle_hierarchy
            
    
def getFamilyHierarchy(suite_json, cycles):
    ancestors = suite_json["ancestors_pruned"]
    cycle_vals = {}
    groupings = {}
    for cycle, jobs in sorted(cycles.items()):
      cycle_vals[cycle] = JobNode(cycle, Job(**{'label' : cycle}))
      cycle_root = cycle_vals[cycle]
      
      for job in jobs:
        order = ancestors[job.name]
        
        # if the job has a family parent
        if (len(order) > 2):
          for element in reversed(order[1:-1]):
            if element + cycle_root.name not in groupings:
              groupings[element + cycle_root.name] = JobNode(element, Job(), parent = cycle_root)
              
            job = JobNode(job.name + job.label, job, parent = groupings[element + cycle_root.name])
          
        # otherwise job just goes under cycle point
        else:
          job = JobNode(job.name + job.label, job, parent = cycle_root)
          
    return cycle_vals

def parseJobs(suite_json):
    jobs = []
    index = 0
    # import pprint
    # pprint.pprint(suite_json)
    for job, job_dict in suite_json["summary"][1].items():
        jobs.append( Job(**job_dict) )
        # print(jobs[index])
        index += 1
    return jobs

def getVerify(suite, path=None):
    """Return the server certificate if possible."""
    
    # return "/home/ubuntu/workspace/cylc_webapp/cylc-variables/"+suite+"/ssl.cert"
    return "/home/ubuntu/cylc-run/" + suite + "/.service/ssl.cert"
    # need to make it so that the user can add the ssl & passphrase to a suite folder.

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
                print("%s%s" % (pre, node.name))
            
            return jobs
        except Exception, err: 
            print err
            
# getResponse()