from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name=models.CharField(max_length=70)
    last_name=models.CharField(max_length=70)
    instrument=models.CharField(max_length=70)

class Album(models.Model):
    artist=models.ForeignKey(Musician,on_delete=models.CASCADE)
    name=models.CharField(max_length=70)
    release_date=models.DateField()
    rating=(
        (1,'worst'),
        (2,'bad'),
        (3,'average'),
        (4,'good'),
        (5,'excellent')
    )
    num_stars=models.IntegerField(choices=rating)
    