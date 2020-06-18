from django.urls import path, reverse
from . import views

urlpatterns = [
    path('sendEmail', views.sendEmail, name='sendEmail')
]