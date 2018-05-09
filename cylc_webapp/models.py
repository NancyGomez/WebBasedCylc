# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# (Nancy) TODO:  Create Job class
# class Connection_Data(models.Model):
    # host = models.CharField(max_length=100)
    # port = models.IntegerField()
    # cert = models.CharField(max_length=256) #this might not be big enough?
    # p_phrase = models.CharField(max_length=256)
    # suite_name = models.CharField(max_legth=256)

# class Job(models.Model):
#     name = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     host = models.CharField(max_length=50)
#     job_system = models.CharField(max_length=50)
#     job_ID = models.IntegerField()
#     t_submit = models.CharField(max_length=50)
#     t_start = models.CharField(max_length=50)
#     t_finish = models.CharField(max_length=50)
#     dt_mean = models.CharField(max_length=50)
#     latest_message = models.CharField(max_length=100)