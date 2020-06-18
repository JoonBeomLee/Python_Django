from django.urls import path, reverse
from . import views

urlpatterns = [
    path('', views.index, name='main_index'),
    path('result', views.result, name='main_result'),
]