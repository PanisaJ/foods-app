from django.contrib import admin

from .models import Restaurant, Review, Menu, Category

admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(Menu)
admin.site.register(Category)
