from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
# Create your models here.
