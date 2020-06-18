from django.urls import path, reverse
from . import views

urlpatterns = [
    path('', views.excelCalcDo, name='excelCalcDo'),
    path('result', views.excelResult, name='excelResult'),
]