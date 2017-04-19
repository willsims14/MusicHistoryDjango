import datetime

from django.db import models
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=30)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=40)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.name) + " by " + str(self.artist) + " on " + str(self.album) + "( " + str(self.genre) +  " )")


