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
    done_to_do = to_do.objects.filter(id=done_id)[0]

    done_to_do.is_done = True
    done_to_do.save()

    return HttpResponseRedirect(reverse('index'))

def chnDone(request):
    chn_id = request.GET['toDo_id']
    chn_to_do = to_do.objects.filter(id=chn_id)[0]

    chn_to_do.is_done = False
    chn_to_do.save()

    return HttpResponseRedirect(reverse('index'))

def delToDo(request):
    del_id = request.GET['toDo_id']
    del_to_do = to_do.objects.get(id=del_id)
    del_to_do.delete()

    return HttpResponseRedirect(reverse('index'))