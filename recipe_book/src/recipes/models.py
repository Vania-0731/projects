from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    steps = models.TextField()
    cook_time = models.IntegerField(help_text="time in minutes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
