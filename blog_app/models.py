from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    flavor_text = models.CharField(max_length=128, default=" ")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Contact(models.Model):
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    flavor_text = models.CharField(max_length=128, default=" ")


class Project(models.Model):
    cover_image = models.CharField(max_length=200, null=True)
    image_alt = models.CharField(max_length=128, default=" ")
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    flavor_text = models.CharField(max_length=128, default=" ")
