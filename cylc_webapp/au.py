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
hname = 'bigbrotherx52-cylc-capstone-sp18-5942931'
suite = "my.suite"
from port import getPorts

# to be used to pull variable from opening page.

hostName = hname
portList = getPorts()


newpath = r'cylc_webapp/cylc-variables' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

passphraseFile = "cylc_webapp/cylc-variables/"+ suite +"/passphrase"
# passphraseFile = "~/home/ubuntu/cylc-run/my.suite/.service/passphrase"


# read passphrase file
with open(passphraseFile,'r') as f:
   	passphrase = f.readline()

def parseJobs(suite_json):
    jobs = []
    index = 0
    for job, job_dict in suite_json[1].items():
        jobs.append( Job(**job_dict) )
        index += 1
    return jobs

def _get_verify():
    """Return the server certificate if possible."""
    
    return "cylc_webapp/cylc-variables/"+suite+"/ssl.cert"
    # return "/home/ubuntu/cylc-run/my.suite/.service/ssl.cert"
    # need to make it so that the user can add the ssl & passphrase to a suite folder.

def getResponse():
    # portNumber = portList[0]
    auth = requests.auth.HTTPDigestAuth('cylc', passphrase)
    session = requests.Session()
    for portNumber in portList:
        url = "https://%s:%d/get_suite_state_summary" % (hostName, portNumber)
        try:
            ret = session.get(
                                url,
                                auth=auth,
                                verify=_get_verify()
                             )
        
            response = ret.json()
            print(response)
            jobs = parseJobs(response)
            return jobs
        except Exception, err: 
            print err