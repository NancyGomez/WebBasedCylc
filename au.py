'''
    FILE: au.py
    PURPOSE: establish secure connection to cylc running instance
    PRECONDITIONS: A running instance of CYLC, the hostname, port number, passphrase,
    and certificate of the suite. Iorder to view these simply check your "concat"
    file within your suite folder. Might be something like cylc-run/my.suite/.services
'''

import requests
import json
from job import Job
from os.path import expanduser

# TODO: change to your host
hostName = 'nancy-VirtualBox'
# TODO: make sure your port is correct (changes every time you run a suite)
portNumber = 43082
# TODO: make sure you change this to your path to your passphrase
passphraseFile = "/home/nancy/cylc-run/my.suite/.service/passphrase"


# read passphrase file
with open(passphraseFile,'r') as f:
   	passphrase = f.readline()

url = "https://%s:%d/get_suite_state_summary" % (hostName, portNumber)
auth = requests.auth.HTTPDigestAuth('cylc', passphrase)
session = requests.Session()


def parseJobs(suite_json):
    jobs = []
    index = 0
    for job, job_dict in suite_json[1].items():
        jobs.append( Job(job_dict) )
        jobs[index].printJob()
        index += 1
        # uncomment to view raw json
        # print "JOB ", job
        # for k, v in value.items():
        #     print k, v, '\n'
    return jobs

def _get_verify():
    """Return the server certificate if possible."""
    return "/home/nancy/cylc-run/my.suite/.service/ssl.cert"

ret = session.get(
                    url,
                    auth=auth,
                    verify=_get_verify()
                )

response = ret.json()
jobs = parseJobs(response)
