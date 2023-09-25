from django.db import models

# Create your models here.


class Finch(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    continent = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.id}'