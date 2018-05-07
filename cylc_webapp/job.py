'''
    FILE: job.py
    PURPOSE: create a class to define a job's attributes
    PRECONDITIONS: A default constructor is provided but requires the dictionary response from
'''
from anytree import NodeMixin, RenderTree

class Job:

    def __init__(self, **kwargs):
        self.name = ""
        self.label = ""
        self.state = ""
        self.host = "N/A"
        self.batch_sys_name = ""
        self.submit_method_id = 0
        self.submitted_time_string = ""
        self.started_time_string = ""
        self.finished_time_string = ""
        self.mean_elapsed_time = ""
        self.latest_message = ""
        self.__dict__.update(kwargs) 
    
    def as_dict(self):
        return self.__dict__
    
    def junk_fill(self):
        self.name = "temp"
        self.label = "temp"
        self.state = "temp"
        self.host = "N/A"
        self.batch_sys_name = "temp"
        self.submit_method_id = 0
        self.submitted_time_string = "0"
        self.started_time_string = "0"
        self.finished_time_string = "0"
        self.mean_elapsed_time = "0"
        self.latest_message = "Epson"
       
    def __repr__(self):
        return self.name + self.label
    
    def __str__(self):
        f = ("Name: {}\nLabel: {}\nState: {}\nHost: {}\nJob System: {}\nJob ID: {}\nLatest Message: {}"
            "\n-- Times --\nSubmitted: {}\nStarted: {}\nFinished: {}\ndT_mean: {}\n")
        return f.format(self.name, self.label, self.state, self.host, self.batch_sys_name, self.submit_method_id, self.latest_message, self.submitted_time_string, self.started_time_string, self.finished_time_string, self.mean_elapsed_time)
        
        
        
class JobNode(Job, NodeMixin):
  def __init__(self, name, Job, parent = None):
    super(JobNode, self).__init__()
    self.name = name
    self.job = Job
    self.parent = parent