from django.db import models
from musician.models import MusicianModel

# Create your models here.

class AlbumModel(models.Model):
    album_name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])
    muscian = models.ForeignKey(MusicianModel, on_delete=models.CASCADE ,related_name='albums')

    # ForeignKey is a type of field in Django that creates a many-to-one relationship. This means that each Album is related to one Musician, 
    # but a single Musician can have multiple Albums

    def __str__ (self):
        return f"{self.album_name} by {self.muscian.first_name}"