from django.urls import path, reverse
from . import views

urlpatterns = [
    path('signIn', views.signIn, name='user_signIn'),
    path('signUp', views.signUp, name='user_signUp'),
    path('signUp/join', views.join, name='user_join'),
    path('verifyCode', views.verifyCode, name='user_verifyCode'),
    path('verify', views.verify, name='user_verify'),
    path('login', views.login, name='user_login'),
    path('logout', views.logout, name='user_logout'),
    path('loginFail', views.loginFail, name='user_loginFail'),
]