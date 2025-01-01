from django.db import models
from django.urls import reverse
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    number = models.IntegerField()
    massage = models.TextField()


    def __str__(self):
        return self.name


class Banner(models.Model):
    name = models.CharField(max_length=100)
    prise = models.IntegerField()
    img = models.ImageField(upload_to='banner/')

    def __str__(self):
        return self.name


class Catagary(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    prise = models.IntegerField()
    prise2 = models.IntegerField()
    img = models.ImageField(upload_to='catagary/')

    def __str__(self):
        return self.name

class Camputers(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    prise = models.IntegerField()
    prise2 = models.IntegerField()
    img = models.ImageField(upload_to='camputers/')
    slug = models.SlugField(max_length=100)

    def get_absolute_url(self):
        return reverse("computersDatailView",args=[self.slug])

    def __str__(self):
        return self.name

class Mansclothers(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    prise = models.IntegerField()
    img = models.ImageField(upload_to='mansclother/')

    def __str__(self):
          return self.name


class Woman(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='woman/')

    def __str__(self):
        return self.name




