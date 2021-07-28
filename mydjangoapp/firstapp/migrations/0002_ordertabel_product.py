# Generated by Django 3.2.5 on 2021-07-27 12:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrderTabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=datetime.datetime(2021, 7, 27, 12, 43, 33, 320297))),
                ('status', models.CharField(default='Placed', max_length=200)),
                ('cartitem', models.TextField()),
                ('price', models.IntegerField()),
                ('addres', models.TextField()),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.user')),
            ],
        ),
    ]
