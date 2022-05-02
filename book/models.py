from django.db import models

# Create your models here.

class sample(models.Model):
    id=models.SmallIntegerField(primary_key=True)
    id1=models.IntegerField()
    id2=models.BigIntegerField()
    id3=models.PositiveIntegerField()
    id4=models.PositiveSmallIntegerField()
    id5=models.PositiveBigIntegerField()
    id6=models.FloatField()
    id7=models.DurationField()
    id8=models.DecimalField(max_digits=5,decimal_places=5)

    id9=models.BinaryField()
    id10=models.BooleanField()


    name=models.CharField(max_length=50)
    name1=models.TextField()
    name3=models.EmailField()
    name4=models.GenericIPAddressField()
    name5=models.URLField()
    name6=models.UUIDField()

    date=models.TimeField()
    date1=models.DateField()
    date2=models.DateTimeField()

    img=models.ImageField()
    img1=models.FileField()

class cont(models.Model):
    demo=models.BigAutoField(primary_key=True)
    #demo1=models.SmallAutoField()
    id =models.CharField(max_length=50,unique=True)
    id1=models.CharField(max_length=50,null=True)
    id2=models.CharField(max_length=50,default="value")
    sample=models.ForeignKey(sample,on_delete=models.CASCADE)


class regi(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.BigIntegerField()
    

class text(models.Model):
    name=models.IntegerField()
    

