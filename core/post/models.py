from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150, null=False)
    slug = models.SlugField(unique=True, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User,  on_delete=models.CASCADE, null=False)

    title = models.CharField(max_length=150, null=False)
    slug = models.SlugField(unique=True, null=False)
    subtitle = models.CharField(max_length=150, null=False)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='images/', null=True)
    text = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


