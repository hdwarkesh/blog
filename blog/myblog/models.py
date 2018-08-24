from django.db import models
from datetime import datetime
# Create your models here.

class Author(models.Model):
    author_name = models.TextField(max_length=50)
    author_city = models.TextField(max_length=15)

class Article(models.Model):
    title = models.TextField(max_length=100)
    body = models.
