from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('createToDo.html', views.createToDo, name='createToDo'),
]