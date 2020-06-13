# Django
## 프로젝트 생성
> django-amdin startproject PROJECT_NAME   
> 생성할 프로젝트명 PROJECT_NAME 위치에 작성    

## 프로젝트 실행
> python manage.py runserver    

## ToDoList 만들기
> MVC패턴   
> (Model, View, Controller)   
>
> CRUD   
> (Create, Read, Update, Delete)   

## App 생성
> 하나의 프로젝트는 여러 개의 app으로 분할 구성   
> python manage.py startapp APP_NAME   
> 생성할 App명 APP_NAME 위치에 작성 (구성할 프로젝트 폴더에서 명령어 실행)   

## App 등록
> 프로젝트명으로 생성된 폴더안 Settings.py 수정   
> ```
> ISTALLED_APPS = [
>    '''''
>    '''''
>    'add_your_app' // 생성한 App추가
> ]
> ```

## URL
> 사용자가 접속할 수 있는 주소   
> 프로젝트명으로 생성된 폴더안 urls.py 수정   
>
> app으로 분할 되어 있을 경우   
> from django.urls import path, include 모듈을 사용   
> ```
> urlpatterns = [
>   '''''''
>   path('your_path', include('your_apps.urls')) // 생성한 App 경로 추가   
> ]
> ```   
> ** 그러나 생성한 app에는 아직 urls.py가 존재하지 않는다.    
> ```
> your_apps > urls.py
> from django.urls import path
> from . import views
> 
> urlpatterns = [
>   path('your_path', views.index),     // path로 접근시 보여줄 페이지 지정   
> ]
> ```
> ** 그러나 생성한 app에는 아직 views.py가 비어있다.

## Views
> url에서 지정한 경로로 접근시 보여줄 페이지를 연결하는 기능   
> ```
> your_apps > views.py
> from django.shortcuts import render
> 
> def index(request):
>    return render(request, 'your.html') // templates 폴더의 html 파일 호출
> ```

## Templates
> app 폴더에 templates 폴더 생성 // 기본은 생성 안되있음   
> templates > your.html   