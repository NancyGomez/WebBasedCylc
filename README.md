# WebBasedCylc

Bringing Cylc to the web by allowing users to skip the hassles of installing all the necessary software required to get Cylc up and running. Simply register your suite and watch it update. (Registration still not implemented, requires storing registered suites in a database)


## Getting Started

### Installing Cylc

Follow the [documentation](https://cylc.github.io/cylc/html/multi/cug-htmlse3.html)
And if you're on windows, here is a special [google doc](https://docs.google.com/document/d/10rI3ESkAkvQb4Pb1mU6Xa4Icx0EW2NoP0uZFfJ9VpLY/edit?usp=sharing) with step by step instructions

### Creating a Cylc instance

Follow the [documentation](https://cylc.github.io/cylc/documentation.html#create-a-new-suite)

### Runnng the Code

Run the workspace in Cloud9 once the suite is already up and running. View the html file `suite_view.html` to ensure it's behaving as expected. 

![Sample Suite View]()


## Prerequisites

1. **Cylc installed** `cylc`
2. **Cylc suite running** `cylc scan -s`  If nothing prints you need to run your instance `cylc run <SUITE NAME>`
3. **Suite's port is within the range checked within `port.py`** `cylc get-suite-contact <SUITE NAME>`
4. **Certificate and passphrase files within path in `au.py`** If you don't know where your suite folder is, simply find it with the following command: `find ~ -name <SUITE NAME>` Then, append`.service` to get the required path. `<PATH GIVEN>/.service`

## Contributing 

### Important Files

**Backend Files:**

* `cylc_webapp/au.py` 
  * Contains API call to retrieve the data, parses it, and organizes it to its hierarchical design defined by cycle point and family relationship. The `getResponse()` returns this parsed data as a dictionary (couldn't seem to traverse the tree structure in the front end so had to simplify it, but it be best used as a tree).

* `cylc_webapp/job.py` 
  * Holds the Job and JobNode class that defines the objects for each job instance in a suite.

* `cylc_webapp/port.py`
  * Contains the script that checks what ports are open and having a running instance. 

* `cylc_webapp/views.py`  sending data to frontend

**Frontend Files:**

* `cylc_webapp/jinja2/templates/`
  * Contains all the front end files including the main file `suite_view.html`, the other html files are unfinished but contain the base for future work. 
