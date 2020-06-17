from django.urls import path, reverse
from . import views

urlpatterns =[
    path('send/', views.sendEmail, name='sendEmail'),
]