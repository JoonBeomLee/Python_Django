from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.
def index(request):
    ctgs = category.objects.all()
    rests = restaurant.objects.all()

    context = {
        'categories':ctgs,
        'restaurants':rests,
    }
    return render(request, 'index.html', context)

def rstDetail(request):
    rst_id = request.GET['rst_id']
    rst = restaurant.objects.get(id=rst_id)

    context = {
        'restaurant': rst,
    }
    return render(request, 'restaurantDetail.html', context)

def rstUpdate(request):
    rst_id = request.GET['rst_id']
    ctgs = category.objects.all()
    rest = restaurant.objects.get(id=rst_id)

    context = {
        'categories':ctgs,
        'restaurant':rest,
    }
    return render(request, 'restaurantUpdate.html', context)

def rstDelete(request):
    rst_id = request.POST['rst_id']
    del_rst = restaurant.objects.get(id=rst_id)
    del_rst.delete()

    return HttpResponseRedirect(reverse('index'))

def rstUpdateDo(request):
    rst_id = request.POST['rstId']
    edit = restaurant.objects.get(id=rst_id)

    edit.category = category.objects.get(id=request.POST['resCategory'])
    edit.rst_name = request.POST['resTitle']
    edit.rst_link = request.POST['resLink']
    edit.rst_content = request.POST['resContent']
    edit.rst_keyword = request.POST['resLoc']

    edit.save()
    re_url = "/restaurantDetail/?rst_id="+rst_id

    return HttpResponseRedirect(re_url)

def rstCreate(request):
    ctgs = category.objects.all()
    
    context = {
        'categories':ctgs,
    }
    return render(request, 'restaurantCreate.html', context)

def rstCreateAdd(request):
    ctg_id = request.POST['resCategory']
    ctg = category.objects.get(id=ctg_id)

    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']

    new_res = restaurant(category=ctg, rst_name=name, rst_link=link, rst_content=content, rst_keyword=keyword)
    new_res.save()

    return HttpResponseRedirect(reverse('index'))

def ctgCreate(request):
    ctgs = category.objects.all()
    context = {
        'categories':ctgs
    }
    return render(request, 'categoryCreate.html', context)

def ctgCreateAdd(request):
    new_ctg_name = request.POST['categoryName']
    new_ctg = category(category_name=new_ctg_name)
    new_ctg.save()

    return HttpResponseRedirect(reverse('index'))

def ctgCreateDel(request):
    del_ctg_id = request.POST['categoryId']
    del_ctg = category.objects.get(id=del_ctg_id)
    del_ctg.delete()

    return HttpResponseRedirect(reverse('ctgCreate'))