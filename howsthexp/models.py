from django.db import models
from hashing import *
from datetime import date

# Create your models here.
class UserRegister(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    username=models.CharField(max_length=8,unique=True)
    password=models.CharField(max_length=5000,default="")

    def __str__(self):
        return f'{self.fn},{self.username},{self.ph_no},{self.email}'



class Song(models.Model):
    title = models.CharField(max_length=100)
    songfile = models.FileField()
    duration = models.FloatField()
    isPlaying = False

    def __str__(self):
        return self.title
