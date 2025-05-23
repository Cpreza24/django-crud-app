from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Candy(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='candies')

    class Meta:
        verbose_name_plural = "Candies"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.type})"
