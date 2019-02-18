from django.shortcuts import render, get_list_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Restaurant, Category

def index(request):
    category_list = Category.objects.all()
    return render(request,'foods/index.html',{'category_list':category_list})

def search(request):
    category = Category.objects.get(category_text=request.POST['category'])
    return HttpResponseRedirect(reverse('result',args=(category.id,)))

def result(request,category_id):
    restaurant_list = get_list_or_404(Restaurant,category__pk=category_id)
    return render(request,'foods/result.html',{'restaurant_list':restaurant_list})
    

