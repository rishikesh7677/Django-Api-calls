# Generated by Django 3.2.5 on 2021-07-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_alter_ordertabel_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertabel',
            name='time',
            field=models.DateTimeField(),
        ),
    ]