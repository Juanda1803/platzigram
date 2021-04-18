# Django
from django.http import HttpResponse , JsonResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
  now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
  return HttpResponse("<h1>Oh, hi! Current server time is {now}</h1>".format(
    now=str(now)
    ))


def sort_integers(request):
  # import pdb;pdb.set_trace
  queries = request.GET['numbers'].split(',')
  numbers = list(map(lambda num: int(num),queries))
  order_numbers = sorted(numbers)
  data ={
    'status':'ok',
    'numbers': order_numbers,
    'message':'Integers sorted successfully'
  }

  # return JsonResponse(dict(enumerate(order_numbers)))
  # return HttpResponse(str(order_numbers), content_type='application/json')
  return HttpResponse(
    json.dumps(data,indent=4),
    content_type='application/json'
    )

def say_hi(request, name, age):
  if age < 12:
    message = 'Sorry {}, you are not allowed here'.format(name)
  else:
    message = 'Hello, {}! Welcome to Platzigram'.format(name)

  return HttpResponse(str(message))