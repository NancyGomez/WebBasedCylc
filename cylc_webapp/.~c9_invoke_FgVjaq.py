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
import socket 
import sys
import time


# TODO: change to your host
hostName = 'bigbrotherx52-cylc-capstone-sp18-5942931'
# TODO: make sure your port is correct (changes every time you run a suite)
# Nathan Put in Port Checker
# ********************************
start_port = 43001
end_port = 43101
host = "localhost"
ip = socket.gethostbyname(host)
open_ports = []
starting_time = time.time()
portNumbers = []

def check_port(host, port, result=1):
    try:
        url = "https://%s:%d/id/identify" % (host, port)

        # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # sock.settimeout(0.5)
        # r = sock.connect_ex((host, port))
        # if r == 0:
        #     result = r
        # sock.close()
    except Exception:
        
        pass

    return result


for p in range(start_port, end_port + 1):
    # sys.stdout.flush()
    try:
        print p,
    except Exception:
        print ".....error something went wrong"
    response = check_port(host, p)
    if response == 0:
        open_ports.append(p)
    if not p == end_port:
        sys.stdout.write('\b' * len(str(p)))
# This will print out how long it takes
# ******************************************************
print "\nScanning completed at %s" % (time.strftime("%I:%M:%S %p"))
ending_time = time.time()
total_time = ending_time - starting_time
print "=" * 40
print "\tScan Report: %s" % host
print "=" * 40
if total_time <= 60:
    total_time = str(round(total_time, 2))
    print "Scan Took %s seconds" % total_time
else:
    total_time = total_time / 60
    print "Scan Took %s Minutes" % total_time
# *****************************************
if open_ports:
    print "Open Ports: "
    for i in sorted(open_ports):

        print "\t%s : Open" % i
        portNumbers.append(i)
       
else:
    print "Sorry, No open ports found.!!"

print portNumbers
# TODO now is take the hidden URL and run it through the loop with the port numbers.
# do not check to see if the port is open you will always get a closed port. 
# will need to send out request will get only a simple message back. if fail or get an error go to next port 
try:
    portNumber = portNumbers[1]

# This line above will need to be set so 
# that it cycles through if it doesn't work the first time

#*********************************
# portNumber = 43013
# TODO: make sure you change this to your path to your passphrase
passphraseFile = "/home/ubuntu/cylc-run/my.suite/.service/passphrase"


# read passphrase file
with open(passphraseFile,'r') as f:
   	passphrase = f.readline()

# url = "https://%s:%d/id/identify" % (hostName, portNumber)
url = "https://%s:%d/get_suite_state_summary" % (hostName, portNumber)
auth = requests.auth.HTTPDigestAuth('cylc', passphrase)
session = requests.Session()


def parseJobs(suite_json):
    jobs = []
    index = 0
    for job, job_dict in suite_json[1].items():
        jobs.append( Job(job_dict) )
        # jobs[index].printJob()
        index += 1
        # uncomment to view raw json
        # print "JOB ", job
        # for k, v in value.items():
        #     print k, v, '\n'
    return jobs

def _get_verify():
    """Return the server certificate if possible."""
    return "/home/ubuntu/cylc-run/my.suite/.service/ssl.cert"

def getResponse():
    ret = session.get(
                        url,
                        auth=auth,
                        verify=_get_verify()
                     )
    
    response = ret.json()
    jobs = parseJobs(response)
    return jobs