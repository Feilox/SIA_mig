from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField()
    director = models.CharField(max_length=150)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title
