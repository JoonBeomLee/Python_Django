from django.urls import path, reverse
from . import views

urlpatterns =[
    path(r'sign', views.sign, name='sign'),
    path(r'signDo', views.signDo, name='signDo'),
    path(r'loginDo', views.loginDo, name='loginDo'),
    path(r'logout', views.logout, name='logout')
]