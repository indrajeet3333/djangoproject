# Generated by Django 2.1.5 on 2019-01-11 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patiladmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='dateofvisit',
            field=models.DateField(default=datetime.datetime(2019, 1, 11, 11, 9, 57, 625095)),
        ),
    ]
