from django.db import models
from musician.models import Musician_Model



# Create your models here.

ratings=[
    (1,'1 Star'),
    (2,'2 Star'),
    (3,'3 Star'),
    (4,'4 Star'),
    (5,'5 Star')
]

class Album_model(models.Model):
    album_name=models.CharField(max_length=50)
    musician_name=models.ForeignKey(Musician_Model,on_delete=models.CASCADE)
    album_relese_date=models.DateTimeField(auto_now=True)
    ratings=models.IntegerField(choices=ratings)

    def __str__(self):
        return self.album_name