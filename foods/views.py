from django.shortcuts import render, HttpResponse

from .models import Restaurant, Category, Menu, Review

def index(request):
    restaurant_list = Restaurant.objects.all()
    return render(request,'foods/index.html',{'restaurant_list':restaurant_list})
