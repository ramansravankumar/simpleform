from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email=models.EmailField(max_length=254,null=True)
    dob=models.DateField(null=True)
