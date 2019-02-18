from django.db import models

class Category(models.Model):
    category_text = models.CharField(max_length=100)
    def __str__(self):
        return self.category_text

class Restaurant(models.Model):
    restaurant_text = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    location = models.TextField(null=True)
    contact = models.TextField(null=True)
    scores = models.IntegerField(default=0)
    average_cost = models.IntegerField(default=0)
    def __str__(self):
        return self.restaurant_text

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    review_text = models.TextField(null=True)
    username = models.CharField(max_length=100)
    scores = models.IntegerField(default=0)

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_text = models.CharField(max_length=100)
    cost = models.IntegerField(default=0)
    def __str__(self):
        return self.menu_text


