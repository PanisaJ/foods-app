from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.searchRestaurant, name='searchRestaurant'),
    path('find/', views.findRestaurant, name='findRestaurant'),
    path('newRestaurant/', views.newRestaurant, name='newRestaurant'),
    path('addRestaurant/', views.addRestaurant, name='addRestaurant'),
    path('newMenu/', views.newMenu, name='newMenu'),
    path('addMenu/', views.addMenu, name='addMenu'),
    path('<int:restaurant_id>/detail/', views.detail, name='detail'),
    path('<int:restaurant_id>/review/', views.review, name='review'),
]
