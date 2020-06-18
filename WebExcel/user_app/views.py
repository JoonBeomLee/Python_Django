from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
# 이메일 인증 후 변경 위함
from user_app.models import *

# 회원 가입시 PWD 암호화
import hashlib

# random 숫자
from random import *

# my sendEmail_app import view
from sendEmail_app.views import * 

# Create your views here.
def signIn(request):
    return render(request, 'signIn.html')

def signUp(request):
    return render(request, "signUp.html")

def join(request):
    Id = request.POST['signUpId']
    name = request.POST['signUpName']
    email = request.POST['signUpEmail']
    password = request.POST['signUpPw']

    # pwd encryption
    # hsah함수 사용 -> import hashlib 문구 필요
    encoded_pwd = password.encode()
    encrypted_pwd = hashlib.sha256(encoded_pwd).hexdigest()

    # pwd = encrypted_pwd 
    # hash함수 사용해 암호화된 pwd 전달
    new_user = User(usr_id=Id, pwd=encrypted_pwd, name=name, email=email)
    new_user.save()

    code = randint(1000, 9999)
    response = redirect('user_verifyCode')
    response.set_cookie('code', code)
    response.set_cookie('user_id', new_user.id)
    
    # my sendEmail_app send function
    # parameters(receiver, verifyCode)
    # return Success:true | Fail:False
    send_result = send(email, code)
    
    if send_result:
        return response
    else:
        context={
            'message':'이메일 발송에 실패했습니다.'
        }
        return render(request, 'error.html', context)
    #return redirect('user_verifyCode')

def verifyCode(request):
    return render(request, 'verifyCode.html')

def verify(request):
    input_code = request.POST['verifyCode']
    cookie_code = request.COOKIES.get('code')

    # 인증번호 일치
    if(input_code == cookie_code):
        user = User.objects.get(id=request.COOKIES.get('user_id'))
        user.validate = 1       # 인증 True
        user.save()

        response = redirect('main_index')
        response.delete_cookie('code')
        response.delete_cookie('user_id')

        # COOKIES 방식
        # response.set_cookie('user', user)

        # SESSION 방식
        request.session['user_id'] = user.usr_id
        request.session['user_email'] = user.email

        return response
    else:
        return redirect('user_verifyCode')

def login(request):
    inpt_id = request.POST['loginID']
    inpt_pw = request.POST['loginPW']

    try:
        user = User.objects.get(usr_id=inpt_id)

        # 입력한 PW를 저장할때 암호화 했던 방식과 동일하게 암호화
        encoded_pwd = inpt_pw.encode()
        encrypted_pwd = hashlib.sha256(encoded_pwd).hexdigest()

        if(user.pwd == encrypted_pwd):
            request.session['user_id'] = user.usr_id
            request.session['user_email'] = user.email

            return redirect('main_index')
        else:
            return redirect('user_loginFail')
    except:
        return redirect('user_loginFail')

def logout(request):
    del request.session['user_id']
    del request.session['user_email']

    return redirect('user_signIn')

def loginFail(request):
    return render(request, "loginFail.html")