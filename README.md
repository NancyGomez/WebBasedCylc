# WebBasedCylc

Bringing Cylc to the web by allowing users to skip the hassles of installing all the necessary software required to get Cylc up and running. Simply register your suite and watch it update.


## Getting Started

TODO

## Prerequisites

TODO check all the installed softwares in the c9 instance

Make sure your cylc instance is running by checking 

`cylc scan -s`

If nothing prints you need to run your instance

`cylc run <SUITE NAME>`

If you haven't made an instance make one. Follow documentation for steps
TODO link documentation

## Contributing 

### Important Files

Backend Files:
* cylc_webapp/au.py - API call, parsing of data 
* cylc_webapp/job.py - Job, JobNode
* cylc_webapp/port.py - port finding
* cylc_webapp/views.py - sending data to frontend

Frontend Files:
* cylc_webapp/jinja2/templates/
