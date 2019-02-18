from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('<int:category_id>/result/', views.result, name='result'),
    path('newRestaurant/', views.newRestaurant, name='newRestaurant'),
]
