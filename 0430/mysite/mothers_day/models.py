from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    date_time = models.DateTimeField('date published')

    def __str__(self):
        return self.name