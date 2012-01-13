from django.db import models

class Post(models.Model):
    message = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')