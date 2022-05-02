from django.db import models

# Create your models here.
class bank(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.TextField()

class bank1(bank):
    pan=models.CharField(max_length=50)
    phone=models.BigIntegerField()

class bank2(bank1):
    adhaar=models.BigIntegerField()
    email=models.EmailField()
    
    