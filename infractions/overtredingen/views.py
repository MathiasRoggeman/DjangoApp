from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import urllib.parse
import os.path
import json
# Create your views here.
    
def index_test(request):
    print('ok')

    return 'Hello world'

