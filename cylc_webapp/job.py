'''
    author: Nancy Gomez
    FILE: job.py
    PURPOSE: Defines the classes Job and JobNode
'''
from anytree import NodeMixin, RenderTree


'''
  Defines a job's attributes named after the JSON response from cylc's suite endpoint
  Also contains is_group, indent, parent_id, and own_id for easier display
'''
class Job:
    '''
      Fills all attributes with the same names with the dictionary info, otherwise
      uses the default values shown below
      @param {**{dict}} kwargs, unpacked dictionary
    '''
    def __init__(self, **kwargs):
        # Information provided by dictionary response
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
        
        # Information used for front end purposes
        self.is_group = False
        self.indent = 0
        self.parent_id = ""
        self.own_id = ""
        
        # Dictionary representation
        self.__dict__.update(kwargs) 
    
    '''
      Returns dictionary representation of a Job
    '''
    def as_dict(self):
        return self.__dict__
    
    '''
      Returns string representation of a Job's attributes
    '''
    def __str__(self):
      if (self.is_group):
        return "Grouping\n"
      else:
        f = ("Name: {}\nLabel: {}\nState: {}\nHost: {}\nJob System: {}\nJob ID: {}\nLatest Message: {}"
            "\n-- Times --\nSubmitted: {}\nStarted: {}\nFinished: {}\ndT_mean: {}\n")
        return f.format(self.name, self.label, self.state, self.host, self.batch_sys_name, self.submit_method_id, self.latest_message, self.submitted_time_string, self.started_time_string, self.finished_time_string, self.mean_elapsed_time)
    
    '''
      Returns simplified string representation of a Job
    '''
    def __repr__(self):
        return self.own_id + self.label
        
''' **************************************************************************************************'''

'''
  Defines a job node that simply has a Job, a unique id, and a JobNode parent
'''
class JobNode(Job, NodeMixin):
  
  '''
    Fill all attributes and set own_id and parent_id of its job instance
    @param {str} id, unique identifier for instance
    @param {Job} job, data that this Node is meant to contain
    @param {JobNode} parent, link to parent instance
  '''
  def __init__(self, id, job, parent = None):
    super(JobNode, self).__init__()
    self.id = id
    self.parent = parent
    self.job = job
    
    self.job.own_id = id
    if (parent is not None):
      self.job.parent_id = parent.id
  
  '''
      Returns string representation of a JobNode which can be either a job or a job grouping
  '''
  def __str__(self):
    if (self.is_group):
        f = ("Id: {}, Grouping")
        return f.format(self.id)
    else:
      f = ("Id: {}, Job: {}")
      return f.format(self.id, repr(self.job))
    