from django.db import models

# Create your models here.

class Musician_Model(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone_number=models.IntegerField(max_length=11)
    instrument_type=models.CharField(max_length=50)

    def __str__(self):
        return self.first_name