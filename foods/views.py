from django.shortcuts import render, HttpResponse

from .models import Restaurant, Category, Menu, Review

def index(request):
    category_list = Category.objects.all()
    return render(request,'foods/index.html',{'category_list':category_list})

def result(request):
    restaurant_list = Restaurant.objects.filter(category__category_text=request.POST['category'])
    return render(request,'foods/result.html',{'restaurant_list':restaurant_list})
