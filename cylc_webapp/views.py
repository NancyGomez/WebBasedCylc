# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from au import getResponse
from job import Job

     

def index(request):
    # jobs = getResponse()
    # return HttpResponse(jobs)
    
    print('here')
    data = getResponse()
    print(data)
    dataset = []
    
    if(data == None):
        d = Job()
        d.junk_fill()
        for i in range(10):
            dataset.append(d.as_dict())
            # print(d)
    else:
        for job in data:
            print(job)
            job = job.as_dict()
            print(job)
        dataset = data
        
    context = {
        'data' : dataset,
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request) )