from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.
def sign(request):
    return render(request, 'sign_copy.html')

def signDo(request):
    usr_id = request.POST['sign_id'] 
    usr_pwd = request.POST['sign_pwd']
    usr_name = request.POST['sign_name']
    usr_email = request.POST['sign_email']

    new_usr = user_info(
        id = usr_id,
        pwd = usr_pwd,
        name = usr_name, 
        email = usr_email
    )
    new_usr.save()

    context ={
        "usr_id":usr_id
    }

    return HttpResponseRedirect('/')

def loginDo(request):
    input_id = request.POST['login_id']
    input_pwd = request.POST['login_pwd']

    sql_result = user_info.objects.filter(id=input_id, pwd=input_pwd)
    if not sql_result: print("fail login")
    else: 
        print("success login")
        request.session['USR_ID'] = input_id

    return HttpResponseRedirect(reverse('index'))

def logout(request):
    request.session['USR_ID'] = None
    request.session.modified=True

    return HttpResponseRedirect(reverse('index'))