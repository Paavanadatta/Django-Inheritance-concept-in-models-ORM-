# Generated by Django 4.0.4 on 2022-04-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_delete_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
