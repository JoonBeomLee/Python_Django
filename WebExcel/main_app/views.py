from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    if 'user_id' in request.session.keys():
        return render(request, 'index.html')
    else:
        return redirect('user_signIn')

def result(request):
    if 'user_id' in request.session.keys():
        return render(request, 'result.html')
    else:
        return redirect('user_signIn')