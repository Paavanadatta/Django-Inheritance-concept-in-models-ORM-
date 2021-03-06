# Generated by Django 4.0.4 on 2022-04-21 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sample',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('id1', models.IntegerField()),
                ('id2', models.BigIntegerField()),
                ('id3', models.PositiveIntegerField()),
                ('id4', models.PositiveSmallIntegerField()),
                ('id5', models.PositiveBigIntegerField()),
                ('id6', models.FloatField()),
                ('id7', models.DurationField()),
                ('id8', models.DecimalField(decimal_places=5, max_digits=5)),
                ('id9', models.BinaryField()),
                ('id10', models.BooleanField()),
                ('name', models.CharField(max_length=50)),
                ('name1', models.TextField()),
                ('name3', models.EmailField(max_length=254)),
                ('name4', models.GenericIPAddressField()),
                ('name5', models.UUIDField()),
                ('date', models.TimeField()),
                ('date1', models.DateField()),
                ('date2', models.DateTimeField()),
                ('img', models.ImageField(upload_to='')),
                ('img1', models.FileField(upload_to='')),
            ],
        ),
    ]
