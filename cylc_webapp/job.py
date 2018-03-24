'''
    FILE: job.py
    PURPOSE: create a class to define a job's attributes
    PRECONDITIONS: A default constructor is provided but requires the dictionary response from
'''


class Job:
    def __init__(self, *args, **kwargs):
        # if argument is passed it's the job_dict
        # TODO:  error check to make sure it's a dictionary
        if (len(args) == 1):
            job_dict = args[0]
            self.name = job_dict["name"]
            self.state = job_dict["state"]
    
            # host may or may not exist!
            self.host = "N/A"
            if ("host" in job_dict):
                self.host = job_dict["host"]
    
            self.job_system = job_dict["batch_sys_name"]
    
            # TODO: double check with code
            self.job_ID = job_dict["submit_method_id"]
    
            self.T_submit = job_dict["submitted_time_string"]
            self.T_start = job_dict["started_time_string"]
            self.T_finish = job_dict["finished_time_string"]
    
            self.dT_mean = job_dict["mean_elapsed_time"]
            self.latest_message = job_dict["latest_message"]
            
        else:
            self.name = ""
            self.state = ""
            self.host = ""
            self.job_system = ""
            self.job_ID = 0
            self.T_submit = ""
            self.T_start = ""
            self.T_finish = ""
            self.dT_mean = ""
            self.latest_message = ""
            
    def __str__(self):
        f = ("Name: {}\nState: {}\nHost: {}\nJob System: {}\nJob ID: {}\nLatest Message: {}"
             "\n-- Times --\nSubmitted: {}\nStarted: {}\nFinished: {}\ndT_mean: {}\n")
        return f.format(self.name, self.state, self.host, self.job_system, self.job_ID, self.latest_message,
                        self.T_submit, self.T_start, self.T_finish, self.dT_mean)

    def printJob(self):
        f = ("Name: {}\nState: {}\nHost: {}\nJob System: {}\nJob ID: {}\nLatest Message: {}"
             "\n-- Times --\nSubmitted: {}\nStarted: {}\nFinished: {}\ndT_mean: {}\n")
        print f.format(self.name, self.state, self.host, self.job_system, self.job_ID, self.latest_message,
                        self.T_submit, self.T_start, self.T_finish, self.dT_mean)