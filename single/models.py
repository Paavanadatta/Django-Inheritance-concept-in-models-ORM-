from django.db import models

# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.BigIntegerField()

class person(details):
    dno=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    pin=models.IntegerField()