# Django
## 프로젝트 생성
> django-amdin startproject PROJECT_NAME   
> 생성할 프로젝트명 PROJECT_NAME 위치에 작성    

## 프로젝트 실행
> python manage.py runserver    

## ToDoList 만들기
> MVC패턴   
> (Model, View, Controller)   
> <img src="https://an4ik.gitbooks.io/be-fullstack/content/assets/images/4.jpg" />   
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

## Model
> models.py 에서 DB의 테이블 단위로 관리   
> 데이터베이스에 대해서 테이블 형태를 정의, 특정 테이블에 대해서 데이터를 저장하거나   
> 필요한 데이터를 꺼내서 사용. 이를 위한 두가지 설정 필요.   
>
> 1. 어떠한 데이터베이스를 사용할 것인지 설정   
>> Django는 기본적으로 SQLite를 사용
>> ```
>> project > settings.py
>> DATABASES = {
>>    'default': {
>>        'ENGINE': 'django.db.backends.sqlite3',
>>        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
>>    }
>>}
>>```
>>MySQL이나 다른 데이터베이스 사용 위해서는 위의 코드를 변경 필요   
>>```
>>DATABASES = {
>>    'default': {
>>        'ENGINE': 'django.db.backends.mysql', #MySQL 엔진 작성
>>        'NAME': 'DB_NAME',        # 사용할 DB 명
>>        'USER': 'USER',           # DB 사용자 ID
>>        'PASSWORD': 'PASSWORD',   # DB 사용자 PWD
>>        'HOST': 'HOST_IP',    # DB 서버 주소
>>        'PORT': 'PORT',       # 3306이 기본
>>    },
>>}
>>```
>
> 2. 테이블에 대한 형태를 정의
>> Table(DB) = Model(Django) = class
>> your_app > models.py 가 역할을 담당.
>> 모델 작성시 DB의 데이터 타입과 일치해야 한다.
>>```
>>class user(models.Model):
>>     id = models.CharField(primary_key=True, max_length=255) // table의 데이터 타입에 맞게 작성
>>    pwd = models.CharField(max_length=30)  // max_length는 255보다 작아야 한다.
>>```

# DB
> DB생성
>> Model에 작성한 내용대로 DB에 적용하기 위한 작업1   
>> ```
>> python manage.py makemigrations <app_name>
>> ```
>> DB가 생성되는 것은 아니다. DB에 적용될 문서가 작성됨.   
>>
>> Model에 작성한 내용대로 DB에 적용하기 위한 작업2   
>> ```
>> python manage.py migrate <app_name>
>> ````
>> 앞서 생성된 migrations 파일을 실제 적용하는 과정.   
>
> DB확인
>> ``` 
>> python manage.py dbshell
>> ```
>> 명령어를 통해 DBshell 접근 가능   
>>
>> Model에 의해 생성된 테이블명은 규칙을 가진다.   
>> 프로젝트명_모델명  ex) to_do_app_user 로 생성이 된다.   