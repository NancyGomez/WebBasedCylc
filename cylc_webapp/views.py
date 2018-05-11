# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from au import getResponse, getSuiteName
from job import Job

  
  
def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

def suites(request):
    template = loader.get_template('suites.html')
    return HttpResponse(template.render())
    
def suite_view(request):
    data = getResponse()
    suite = getSuiteName()
    dataset = []
    dataOrder = ["name", "label", "latest_message","host","batch_sys_name","submit_method_id","submitted_time_string","started_time_string","finished_time_string","mean_elapsed_time"]
    if(data == None):
        d = Job()
        for i in range(10):
            dataset.append(d.as_dict())
    else:
        for job in data:
            job = job.as_dict()
        dataset = data
        
    context = {
        'dataOrderKey' : dataOrder,
        'data' : dataset,
        'suite' : suite
    }
    template = loader.get_template('suite_view.html')
    return HttpResponse(template.render(context, request) )