from os.path import expanduser
import socket 
import sys
import time
import urllib
import urllib2
from au import hname


start_port = 43001
end_port = 43101
host = hname
#  127.0.0.1/8 ip for this 
ip = socket.gethostbyname(host)
open_ports = []
starting_time = time.time()
portNumbers = []

def check_port(host, port, result=1):
    try:
        try:
            proxy_handler = urllib2.ProxyHandler({})
            opener = urllib2.build_opener(proxy_handler)
            url = "https://%s:%d/id/identify" % (host, port)
            req = urllib2.Request(url)
            res = opener.open(req)
            data = res.read()
            print data
        except urllib2.HTTPError, err:
            if err.code == 401:
                # print port, "good response"
                result = 0
                return result
            # else:
                # print err
                # print port, "bad response"
        except urllib2.URLError, err:
            pass
            # print err
            # print port, "bad response"
    except Exception, err:
        print err
    return result


for p in range(start_port, end_port + 1):
        response = check_port(host, p)
        if response == 0:
            open_ports.append(p)
        if not p == end_port:
            sys.stdout.write('\b' * len(str(p)))

def getPorts():
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
        
    return portNumbers
    # TODO now is take the hidden URL and run it through the loop with the port numbers.
    # do not check to see if the port is open you will always get a closed port. 
    # will need to send out request will get only a simple message back. if fail or get an error go to next port 
