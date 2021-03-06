# Generated by Django 4.0.4 on 2022-04-22 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bank',
            fields=[
                ('bid', models.BigAutoField(primary_key=True, serialize=False)),
                ('ifsc', models.CharField(max_length=40)),
                ('si', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='rbi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='bank1',
            fields=[
                ('bank_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='multi.bank')),
                ('rbi_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='multi.rbi')),
                ('pan', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('adhaar', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
            bases=('multi.rbi', 'multi.bank'),
        ),
    ]
