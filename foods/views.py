from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Restaurant, Category, Menu, Review

def index(request):
    category_list = Category.objects.all()
    return render(request,'foods/index.html',{'category_list':category_list})

def findRestaurant(request):
    if request.GET.get('find'):
        restaurant_list = Restaurant.objects.filter(restaurant_text__contains=request.GET['find'])
        if restaurant_list.count() == 0:
            print("not exist")
            category_list = Category.objects.all()
            error_message = "Sorry, no restaurants matched '" + request.GET['find'] + "'. Please try again."
            return render(request,'foods/index.html',{'category_list':category_list,'error_message':error_message,})
        else:
            print("exist")
            for i in restaurant_list:
                print(i.restaurant_text)
            return render(request,'foods/Result.html',{'restaurant_list':restaurant_list})
    else:
        category_list = Category.objects.all()
        return render(request,'foods/index.html',{'category_list':category_list,'error_message':"You didn't insert input.",})

def searchRestaurant(request):
    restaurant_list = Restaurant.objects.filter(category__category_text=request.GET['category'])
    return render(request,'foods/Result.html',{'restaurant_list':restaurant_list})

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
        restaurant = Restaurant.objects.get(restaurant_text=request.POST['restaurant'])
        restaurant.average_cost *= restaurant.menu_set.count()
        menu = Menu()
        menu.menu_text = request.POST.get('menu')
        menu.restaurant = restaurant
        menu.cost = request.POST.get('cost')
        menu.save()
        restaurant.average_cost += int(request.POST.get('cost'))
        restaurant.average_cost /= restaurant.menu_set.count()
        restaurant.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        restaurant_list = Restaurant.objects.all()
        return render(request,'foods/newMenu.html',
               {'error_message':"You didn't insert some inputs.",
                'restaurant_list':restaurant_list,}
        )

def detail(request,restaurant_id):
    restaurant = get_object_or_404(Restaurant,pk=restaurant_id)
    return render(request,'foods/detail.html',{'restaurant':restaurant,'range': range(0,5),})

def review(request,restaurant_id):
    if request.POST.get('review') and request.POST.get('username') and request.POST.get('score'):
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        restaurant.average_scores *= restaurant.review_set.count()
        review = Review()
        review.review_text = request.POST.get('review')
        review.username = request.POST.get('username')
        review.scores = request.POST.get('score')
        review.restaurant = restaurant
        review.save()
        restaurant.average_scores += int(request.POST.get('score'))
        restaurant.average_scores /= restaurant.review_set.count()
        restaurant.save()
        return HttpResponseRedirect(reverse('detail',args=(restaurant_id,)))
    else:
        restaurant = get_object_or_404(Restaurant,pk=restaurant_id)
        return render(request,'foods/detail.html',
                {'restaurant':restaurant,
                 'range': range(0,5),
                 'error_message':"You didn't insert some inputs.",})


