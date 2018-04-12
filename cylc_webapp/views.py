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
    data = getResponse()
    print(data)
    template = loader.get_template('index.html')
    return HttpResponse(template.render())