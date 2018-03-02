#au.py
#needs incorporated with new app.py
import requests
import json
from os.path import expanduser

hostName = 'nancy-VirtualBox'
portNumber = 43086
home = expanduser("~")
#typical non-example suite path
#passphraseFile = home+"/cylc-run/"+suiteName+"/.service/passphrase
#passphraseFile = home+"/cylc-run/examples/7.5.0/tutorial/cycling/one/.service/passphrase"
passphraseFile = "/home/nancy/cylc-run/my.suite/.service/passphrase"
with open(passphraseFile,'r') as f:
   	passphrase = f.readline()
url = "https://%s:%d/get_suite_state_summary" % (hostName,portNumber)
auth = requests.auth.HTTPDigestAuth('cylc', passphrase)
session = requests.Session()



def _get_verify():
    """Return the server certificate if possible."""
    return "/home/nancy/cylc-run/my.suite/.service/ssl.cert"


ret = session.get(
                    url,
                    auth=auth,
                    verify=_get_verify()
                )

print ret.status_code
print json.dumps(ret.json(), indent=4, sort_keys=True)
