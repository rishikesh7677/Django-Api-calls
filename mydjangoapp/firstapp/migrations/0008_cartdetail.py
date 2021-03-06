# Generated by Django 3.2.5 on 2021-07-27 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_alter_ordertabel_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('statusofpd', models.CharField(max_length=200)),
                ('expecteddate', models.DateTimeField()),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.ordertabel')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.product')),
            ],
        ),
    ]
