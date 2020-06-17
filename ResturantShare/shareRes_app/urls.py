from django.urls import path, reverse
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    # <str:rst_id> 자리의 값을 지정한 형태로 페이지로 전달
    path('restaurantDetail/', views.rstDetail, name='rstDetail'),
    path('restaurantDetail/updateRes', views.rstUpdate, name='rstUpdate'),
    path('restaurantCreate/', views.rstCreate, name='rstCreate'),
    path('restaurantCreate/addRes', views.rstCreateAdd, name='addRes'),
    path('categoryCreate/', views.ctgCreate, name='ctgCreate'),
    path('categoryCreate/addCtg', views.ctgCreateAdd, name='addCtg'),
    path('categoryCreate/deleteCtg', views.ctgCreateDel, name='delCtg'),
]