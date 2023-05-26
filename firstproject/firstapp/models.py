from django.db import models

# Create your models here.
class First(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    phoneno=models.IntegerField()
    address=models.CharField(max_length=30)
