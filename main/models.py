from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=1023)
    image = models.FileField(upload_to='media', blank=True)
    date = models.DateTimeField(auto_now=True)
    dsc = models.TextField(max_length=2047, blank=True)
