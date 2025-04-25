from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'my_app'
        db_table = 'my_app_user'

    def __str__(self):
        return self.username

class Candy(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'my_app.User',
        on_delete=models.CASCADE,
        related_name='candies',
        default=1
    )

    class Meta:
        verbose_name_plural = "Candies"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.type})"
