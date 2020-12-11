from django.db import models

from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from PIL import Image


class Profile(models.Model):
    username = models.CharField(max_length=264, blank=True)
    full_name = models.CharField(max_length=264, blank=True)
    profile_pic = models.ImageField(upload_to='farmer_profile_pics')
    address_1 = models.TextField(max_length=300, blank=True)
    city = models.CharField(max_length=40, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='article_pics')

    def __str__(self):
        return f'{self.author} Post'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})




