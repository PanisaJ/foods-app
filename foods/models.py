from django.db import models

class Category(models.Model):
    category_text = models.CharField(max_length=100)

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    location = models.TextField(null=True)
    contact = models.TextField(null=True)
    def __str__(self):
        return self.restaurant_name

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    review_text = models.TextField(null=True)
    username = models.CharField(max_length=100)

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_text = models.CharField(max_length=100)
    cost = models.IntegerField(default=0)
    def __str__(self):
        return self.menu_text


