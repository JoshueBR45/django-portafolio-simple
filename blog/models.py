from django.db import models
import datetime


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    image = models.ImageField(upload_to="blog/images")
    date = models.DateField(datetime.date.today)
def str (self):
    return self.title

# Create your models here.
