from django.db import models

class VideoGame(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
