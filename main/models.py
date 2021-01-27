from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_ad = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)    


class Book(models.Model):
    title = models.CharField(max_length=50)
    subTitle = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    date = models.DateField(auto_now_add=True)