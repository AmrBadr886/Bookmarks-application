from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Link(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url


class Bookmark(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name='bookmarks')

    def __str__(self):
        return self.title
