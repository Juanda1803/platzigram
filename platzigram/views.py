""" Platzigram views. """

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json


def hello(request):
  # Return a gretting
  # Get date -------------- how struct the date !
  now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
  return HttpResponse('Oh, hi! Current server time is {now}'.format(now=str(now)))


def sort_integers(request):
  # Return a JSON  responser with sorted intergers
  # ----------------------------------- "split" separete the number given the character
  numbers = [int(i) for i in request.GET['numbers'].split(',')]
  # "sorted()" recived to list and the ordenation
  sorted_ints = sorted(numbers)
  data = {
    'status': 'ok',
    'numbers': sorted_ints,
    'message': 'Integers sorted successfully'
  }
  #------"-json.dumps()" traduct the dictionary to JSON------------ type headers
  return HttpResponse(json.dumps(data,indent=5), content_type='application/json')


def say_hi(request, name, age):
  # Return a gretting
  if age < 12:
    message = 'Sorry {}, you are allowed here'.format(name)
  else:
    message = 'Welcome {}! to platzi'.format(name) 
  return HttpResponse(message)