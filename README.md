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

# 값 전달
> POST | GET 방식   
> ```
> <form action="your_action_path" method="GET || POST"> {% csrf_token %}
> <input id="your_id" name="your_name" type="text"/>
> ```
> Django에서는 기본적으로 CSRF토큰을 이용해 CSRF공격을 방지한다.   
> CSRF란 Cross Site Request Forgery의 약자로 웹 어플리케이션의 취약점을 이용해   
> 비정상적인 요청을 유발하는 공격방법이다. 이러한 공격예방을 Django에서는 기본 제공한다.    
> * form사용시 작성하도록 한다.
> 
> form 작동시 action의 경로로 페이지는 method의 방식을 따라 값을 전달한다.    
> 따라서 url과 view를 경로에 맞게 추가해준다.   
> ```
> urls.py
> urlpatterns =[
>    """"""
>    path('your_path', views.your_page) # add url
> ]
>
> views.py
> def your_page(request):           # url에 추가해준 함수를 작성
>    # POST | GET for에서 작성한 방식을 통해 값 참조 가능
>    your_var = request.POST['your_name']   # 참조시 태그의 name을 사용한다.
>    context = {"your_var":your_var}        # dict형태로 참조할 id명과 변수를 쌍으로 전달 
>    return render(request, 'your.html', context) # render시 이동할 템플릿과 함께 전달(your_var로 참조 가능)
> ```

# 값 저장
> form에서 전달한 값을 받는법을 확인하였다.   
> 그렇다면 확인한 값을 DB에 저장하는 방법은??   
> 앞서 작성한 Model을 활용한다.   
> ```
> views.py
> from .models import *      # 작성한 Model을 참조하기 위한 import
>
> def yourPage(request):
>    your_var = request.POST['your_name']
>    # add
>    new_Model = your_model(model_var=your_var) # 받은 값을 생성한 모델(class)에 전달
>    new_Model.save()                           # 전달받은 모델을 save() 함수를 통해 DB에 저장
>    return render(request, 'your.html')
> ```

# 값 출력
> 템플릿 태그
> Html을 통한 페이지 내용 작성시 각기 다른 값을 출력하기 위한 태그    
> ```
> {{ var_name }} # 변수 출력 
> 
> {% for for_var in for_vars %}         # for문 시작 태그
>   <h1>반복할 태그 {{ var_name }}</h1>  # 태그 안에서 {{ }} 변수출력 가능
> {% endfor %}                          # for문 종료 태그
>
> {% if your_condition1 %}              # if문 condition에 따른 if기능 수행
>   <h1> 조건 True </h1>
> {% elif your_condition2 %}
>   <h1> 조건2 True </h1>
> {% else %}
>   <h1> 조건1,2 False </h1>
> {% endif %}                           # if문 종료 태그
> ```
> 이 밖에도 다양한 커스텀 태그를 작성할 수 있다.   

# 값 수정
> 앞서 DB를 활용하기 위해서 Model을 작성하였다. Django의 Model에는 object 객체가 제공(model.objects)되는데    
> 이를 통해 해당 모델 클래스의 DB데이터를 추가, 조회, 수정, 삭제(CRUD)을 간편히 수행할 수 있다. ex) 앞서 사용한 new_Model.save()가 추가(C)의 기능이다.
> 
> QuerySet은 Django의 SQL을 생성해주는 인터페이스로 별도의 SQL작성과정 없이    
> DB로 부터 데이터를 가져오고 추가, 수정, 삭제가 가능하다.    
> ```
> new_Model.Objects.all     # SELECT * FROM new_Model… 와 같은 SQL문 생성
> new_Model.Objects.create  # INSERT INTO new_Model VALUES(…) 와 같은 SQL문 생성
>
> # and 조건(filter)
> queryset = 모델클래스명.objects.all()         # filter를 통해 조건에 맞는 데이터 조회
> queryset = queryset.filter(조건필드1=조건값1, 조건필드2=조건값2) # and 조건
> queryset = queryset.filter(조건필드3=조건값3)
>
> # 제외조건 (exclude)
> # 제목에 '테스트'를 포함한 record를 제외한 전체
> Post.objects.all().exclude(title__icontains='test')
> 
> # 제목에 1을 포함하지만 3으로 끝나지 않는 record
> Post.objects.filter(title__icontains='1').exclude(title__endswith='3')
>
> # OR 조건 (filter)
> # Complex lookups with Q objects : or 조건을 사용하기 위해서는 Q 객체 import가 필요하다.   
> from django.db.models import Q
> 
> 모델클래스명.objects.all().filter(Q(조건필드1=조건값1) | Q(조건필드2=조건값2)) # or 조건
> 모델클래스명.objects.all().filter(Q(조건필드1=조건값1) & Q(조건필드2=조건값2)) # and 조건
>
> # 정렬
> queryset = queryset.order_by('field1') # 지정 필드 오름차순 요청
> queryset = queryset.order_by('-field1') # 지정 필드 내림차순 요청
> queryset = queryset.order_by('field2', 'field3') # 1차기준, 2차기준
>
> # 범위 조건 (슬라이싱)
> queryset = queryset[:10] # 현재 queryset에서 처음10개만 가져오는 조건을 추가한 queryset
> queryset = queryset[10:20] # 현재 queryset에서 처음10번째부터 20번째까지를 가져오는 조건을 추가한 queryset
> 
> # 리스트 슬라이싱과 거의 유사하나, 역순 슬라이싱은 지원하지 않음
> queryset = queryset[-10:] # AssertionError 예외 발생
> 
> # 이때는 먼저 특정 필드 기준으로 내림차순 정렬을 먼저 수행한 뒤, 슬라이싱
> queryset = queryset.order_by('-id')[:10]