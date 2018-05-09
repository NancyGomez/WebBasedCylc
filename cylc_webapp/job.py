'''
    FILE: job.py
    PURPOSE: create a class to define a job's attributes
    PRECONDITIONS: A default constructor is provided but requires the dictionary response from
'''
from anytree import NodeMixin, RenderTree

class Job:

    def __init__(self, **kwargs):
        self.name = "*"
        self.label = "*"
        self.state = "*"
        self.host = "*"
        self.batch_sys_name = "*"
        self.submit_method_id = "*"
        self.submitted_time_string = "*"
        self.started_time_string = "*"
        self.finished_time_string = "*"
        self.mean_elapsed_time = "*"
        self.latest_message = "*"
        self.is_group = False
        self.indent = 0
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
        self.indent = 0
        self.is_group = False
       
    def __repr__(self):
      if (self.is_group):
        return self.name
      else:
        return self.name + self.label
    
    def __str__(self):
      if (self.is_group):
        return "Grouping\n"
      else:
        f = ("Name: {}\nLabel: {}\nState: {}\nHost: {}\nJob System: {}\nJob ID: {}\nLatest Message: {}"
            "\n-- Times --\nSubmitted: {}\nStarted: {}\nFinished: {}\ndT_mean: {}\n")
        return f.format(self.name, self.label, self.state, self.host, self.batch_sys_name, self.submit_method_id, self.latest_message, self.submitted_time_string, self.started_time_string, self.finished_time_string, self.mean_elapsed_time)
        
class JobNode(Job, NodeMixin):
  def __init__(self, id, Job, parent = None):
    super(JobNode, self).__init__()
    self.id = id
    self.job = Job
    self.parent = parent
    
  def __str__(self):
    if (self.is_group):
        f = ("Id: {}, Grouping")
        return f.format(self.id)
    else:
      f = ("Id: {}, Job: {}")
      return f.format(self.id, repr(self.job))
    