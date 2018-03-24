##Necessary steps for this to run:

**cylc** command must work (check to see it's in the path if not)

`PATH=$PATH:/home/ubuntu/workspace/cylc/bin`

Next, make sure your cylc instance is running by checking 

`cylc scan -s`

If nothing prints you need to run your instance

`cylc run my.suite`

If you haven't made an instance make one. Follow documentation for steps

Next check port

`cylc get-suite-contact my.suite`

If port is different from the port in au.py, change it in the code

`# TODO: make sure your port is correct (changes every time you run a suite)`

`portNumber = <CHANGE>`