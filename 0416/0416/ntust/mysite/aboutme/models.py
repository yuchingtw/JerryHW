from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=7)
    bitrhday = models.CharField(max_length=8)
    about = models.CharField(max_length=1024)
    photo_link = models.CharField(max_length=1024)
    facebook_link = models.CharField(max_length=1024)
    def __str__(self):
        return self.name
