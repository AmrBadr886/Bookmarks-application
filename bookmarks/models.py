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


class Tag(models.Model):
    title = models.CharField(max_length=64, unique=True)
    bookmarks = models.ManyToManyField(Bookmark, related_name='tags')

    def __str__(self):
        return self.title


class SharedBookmark(models.Model):
    bookmark = models.OneToOneField(Bookmark)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    votes = models.IntegerField(default=1)
    user_voted = models.ManyToManyField(User, related_name='shared_bookmarks')

    def __str__(self):
        return "<%s -%s>" % (self.bookmark, self.votes)
