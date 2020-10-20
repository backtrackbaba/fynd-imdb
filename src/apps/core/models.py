from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.

class MovieInfo(models.Model):
    name = models.TextField(db_index=True, max_length=255)
    director = models.TextField(max_length=255, blank=True)
    popularity = models.FloatField(blank=True)
    imdb_score = models.FloatField(blank=True)
    genres = ArrayField(models.CharField(max_length=1000), default=list, null=True)

    def __str__(self):
        return self.name
