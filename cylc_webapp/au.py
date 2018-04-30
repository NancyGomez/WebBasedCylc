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
from job import Job
from port import getPorts

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
    print cycle_hierarchy
            
    
def getFamilyHierarchy(suite_json):
    ancestors = suite_json["ancestors"]
    ancestors_pruned = suite_json["ancestors_pruned"]
    descendants = suite_json["descendants"]
    
    # TODO: need to parse them in a way where the family hierarchy makes sense
    # import pprint
    # pprint.pprint(ancestors)
    # pprint.pprint(ancestors_pruned)
    # pprint.pprint(descendants)

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
            getFamilyHierarchy(response)
            getCycleHierarchy(jobs)
            return jobs
        except Exception, err: 
            # pass
            print err
            
getResponse()