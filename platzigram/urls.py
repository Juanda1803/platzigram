from django.urls import path
from platzigram import views

urlpatterns = [
    path('hello/', views.hello),
    path('sorted/', views.sort_integers),
    path('hi/<str:name>/<int:age>/', views.say_hi),
]
