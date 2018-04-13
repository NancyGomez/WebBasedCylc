##Necessary steps for this to run:

**cylc** command must work (check to see it's in the path if not)

`PATH=$PATH:/home/ubuntu/workspace/cylc/bin`

Next, make sure your cylc instance is running by checking 

`cylc scan -s`

If nothing prints you need to run your instance

`cylc run my.suite`

If you haven't made an instance make one. Follow documentation for steps

To view running app go to:

https://cylc-capstone-sp18-bigbrotherx52.c9users.io/cylc_webapp/