from pickle import TRUE, UNICODE
from tkinter.tix import Tree
from django.db import models

# Create your models here.
class studentmodel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age= models.IntegerField(default=10)
    email=models.EmailField(unique=True)
    phone=models.BigIntegerField(unique=True)


