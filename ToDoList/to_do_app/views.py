from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def createToDo(request):
    toDo_text = request.POST['toDoContent']
    new_toDo = to_do(content=toDo_text)
    new_toDo.save() 

    context = {"to_do": toDo_text}
    return render(request, 'createToDo.html', context)