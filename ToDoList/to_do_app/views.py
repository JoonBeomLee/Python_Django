from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    return render(request, 'index.html')

def createToDo(request):
    toDo = request.POST['toDoContent']
    new_toDo = toDo(content=toDo)
    new_toDo.save() 
    return render(request, 'createToDo.html')