from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

import import_ipynb
# import testing
# from ipynb.fs.full.testing import test
from testing.practice1 import test, testingdata
# from testing.testing.ipynb import *
# Create your views here.

def home(requests):
    return render(requests, 'dashboard_app/welcome.html')

# @api_view(['POST'])
def testing():
    notebook_output = testingdata()
    return notebook_output
