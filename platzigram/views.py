""" Platzigram views.py """

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

def hello(request):
  # Return a gretting
  now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
  return HttpResponse('Oh, hi! Current server time is {now}'.format(now=str(now)))

def sort_integers(request):
  # Return a JSON  responser with sorted intergers
  numbers = request.GET['numbers']
  return HttpResponse(numbers)

def say_hi(request,name,age):
  # Return a gretting
  if age < 12:
    message = 'Sorry {}, you are allowed here'.format(name)
  else:
    message = 'Welcome {}! to platzi'.format(name) 
  return HttpResponse(message)