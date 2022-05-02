from django.db import models

# Create your models here.
class base(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.BigIntegerField()
    class Meta:
        abstract=True

class student(base):
    course=models.CharField(max_length=40)
    batch=models.CharField(max_length=40)
    fee=models.IntegerField()


class tech(base):
    design=models.CharField(max_length=40)
    sub=models.CharField(max_length=40)
    sal=models.IntegerField()

class nontech(base):
    design=models.CharField(max_length=40)
    sal=models.IntegerField()