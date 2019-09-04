from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import urllib.parse
import os.path
from .models import Infraction
import json
import string
# Create your views here.
 
def index(request):
    json_data = open('infractions\overtredingen\infractions.json')   
    data1 = json.load(json_data) # deserialises it
    data2 = json.dumps(data1) # json formatted string
    json_data.close()
    return data2

def index_test(request):
    return 'Hello world'

