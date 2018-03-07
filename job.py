class Job:
    def __init__(self):
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

    def __init__(self, job_dict):
        self.name = job_dict["name"]
        self.state = job_dict["state"]
        self.host = job_dict["job_hosts"]
        self.job_system = job_dict["batch_sys_name"]
        self.job_ID = job_dict["label"]
        self.T_submit = job_dict["submitted_time_string"]
        self.T_start = job_dict["started_time_string"] # also submitted_time_string ??
        self.T_finish = job_dict["finished_time_string"]
        self.dT_mean = job_dict["mean_elapsed_time"]
        self.latest_message = job_dict["latest_message"]

    def printJob(self):
        print '''Name: %s\nState: %s''' % (self.name, self.state)
