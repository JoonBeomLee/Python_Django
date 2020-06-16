from django.urls import path, reverse
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path(r'saveToDo', views.saveToDo, name='saveToDo'),
    path(r'isDone', views.toDoIsDone, name='isDone'),
]