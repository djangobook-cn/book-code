from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Essay(models.Model):
    title = models.CharField(max_length=128)
    publish_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    show_times = models.IntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ['-publish_time']

    def __str__(self):
        return self.title


class Blog(Essay):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    summary = models.TextField()
    content = models.TextField()


class PurePage(Essay):
    content = models.TextField()
