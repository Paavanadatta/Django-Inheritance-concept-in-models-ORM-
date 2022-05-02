from django.db import models

# Create your models here.
class rbi(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.TextField()

class bank(models.Model):
    bid=models.BigAutoField(primary_key=True)
    ifsc=models.CharField(max_length=40)
    si=models.FloatField()


class bank1(rbi,bank):
    pan=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    adhaar=models.BigIntegerField()
    email=models.EmailField()
