from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=20)
    sal=models.IntegerField()
    dept=models.CharField(max_length=25)
    mtr=models.CharField(max_length=20)

class proxyemployee(employee):
    class Meta:
        proxy=True
