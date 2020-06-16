from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
# usr_info
# from user_app.models import user_info

# Create your views here.
def index(request):
    login_id = request.session['USR_ID']
    context = None
    # login session 유효시
    if login_id:
        toDo_list = to_do.objects.filter(usr_id=login_id).order_by('id').values('content', 'id', 'is_done')
        context ={
            'contents':toDo_list
        }
    return render(request, 'index.html', context=context)

def saveToDo(request):
    toDo_text = request.POST['toDoContent']
    usr_id = request.session['USR_ID']
    new_toDo = to_do(usr_id=usr_id, content=toDo_text)
    new_toDo.save() 

    return HttpResponseRedirect(reverse('index'))

def toDoIsDone(request):
    done_id = request.GET['toDo_id']
    to_do.objects.filter(id=done_id)

    return HttpResponseRedirect(reverse('index'))
