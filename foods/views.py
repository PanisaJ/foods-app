from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Restaurant, Category, Menu

def index(request):
    category_list = Category.objects.all()
    return render(request,'foods/index.html',{'category_list':category_list})

def search(request):
    category = Category.objects.get(category_text=request.POST['category'])
    return HttpResponseRedirect(reverse('result',args=(category.id,)))

def result(request,category_id):
    restaurant_list = get_list_or_404(Restaurant,category__pk=category_id)
    return render(request,'foods/result.html',{'restaurant_list':restaurant_list})
    
def newRestaurant(request):
    category_list = Category.objects.all()
    return render(request,'foods/newRestaurant.html',{'category_list':category_list})

def addRestaurant(request):
    if request.POST.get('restaurant') and request.POST.get('category') and request.POST.get('location') and request.POST.get('contact'):
        restaurant = Restaurant()
        restaurant.restaurant_text = request.POST.get('restaurant')
        restaurant.category = Category.objects.get(category_text=request.POST['category'])
        restaurant.location = request.POST.get('location')
        restaurant.contact = request.POST.get('contact')
        restaurant.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        category_list = Category.objects.all()
        return render(request,'foods/newRestaurant.html',
               {'error_message':"You didn't insert some inputs.",
                'category_list':category_list,}
        )

def newMenu(request):
    restaurant_list = Restaurant.objects.all()
    return render(request,'foods/newMenu.html',{'restaurant_list':restaurant_list})
        
def addMenu(request):
    if request.POST.get('menu') and request.POST.get('restaurant') and request.POST.get('cost'):
        menu = Menu()
        menu.menu_text = request.POST.get('menu')
        menu.restaurant = Restaurant.objects.get(restaurant_text=request.POST['restaurant'])
        menu.cost = request.POST.get('cost')
        menu.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        restaurant_list = Restaurant.objects.all()
        return render(request,'foods/newMenu.html',
               {'error_message':"You didn't insert some inputs.",
                'restaurant_list':restaurant_list,}
        )

def detail(request,restaurant_id):
    restaurant = get_object_or_404(Restaurant,pk=restaurant_id)
    return render(request,'foods/detail.html',{'restaurant':restaurant})
