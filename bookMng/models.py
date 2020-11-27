from django.db import models

from django.contrib.auth.models import User

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.conf import settings

# Create your models here.
class MainMenu(models.Model):
    item = models.CharField(max_length=200, unique=True)
    link = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.item


class Book(models.Model):
    name = models.CharField(max_length=200)
    web = models.URLField(max_length=200)
    price = models.DecimalField(decimal_places=2,max_digits=6)
    publishdate = models.DateField(auto_now=True)
    picture = models.FileField(upload_to='bookEx/static/uploads')
    pic_path = models.CharField(max_length=300, editable=False, blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Request(models.Model):
    name = models.CharField(max_length=200)
    web = models.URLField(max_length=200)
    publishdate = models.DateField(auto_now=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Review(models.Model):
    bookId = models.ForeignKey(Book, blank=True, null=True, on_delete=models.CASCADE)
    rating = models.CharField(max_length=200)
    review = models.TextField(max_length=1000)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    publishdate = models.DateField(auto_now=True)
    # rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    # reviewTitle = models.CharField(max_length=200)


    def __str__(self):
        return str(self.id)

class UserCart(models.Model):
    name = models.CharField(max_length=200, default="Anonymous")
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    bookId = models.ForeignKey(Book, blank=True, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2,max_digits=6,default=0)
    adddate = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.id)