from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def createToDo(request):
    to_do = request.POST['toDoContent']
    return render(request, 'createToDo.html')