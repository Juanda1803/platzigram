# Django
from django.shortcuts import render, HttpResponse

# Utilities
from datetime import datetime


posts = [
  {
    'title': 'Mont Blac',
    'user':{
      'name':'Christian Van der Henst',
      'picture': 'https://picsum.photos/60/60/?image1005'
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo': 'https://picsum.photos/800/800/?image=903'
  },
  {
    'title': 'Mont Blac',
    'user':{
      'name':'Juan Gonzalez',
      'picture': 'https://picsum.photos/60/60/?image1005'
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo': 'https://picsum.photos/800/800/?image=903'
  },
  {
    'title': 'Mont Blac',
    'user':{
      'name':'Christian Van der Henst',
      'picture': 'https://picsum.photos/60/60/?image1005'
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo': 'https://picsum.photos/800/800/?image=903'
  },
  {
    'title': 'Mont Blac',
    'user':{
      'name':'Freddy Vega',
      'picture': 'https://picsum.photos/60/60/?image1005'
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo': 'https://picsum.photos/800/800/?image=903'
  },
]


def list_posts(request):
    # Return list existing
    # Render programming login and recived render(request, HTML-name, dictionary)
    return render(request,'feed.html',{'posts': posts})
