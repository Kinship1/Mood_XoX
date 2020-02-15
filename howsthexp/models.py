from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    songfile = models.FileField()
    duration = models.FloatField()
    isPlaying = False

    def __str__(self):
        return self.title
    
