# Generated by Django 2.1.5 on 2019-01-11 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patiladmin', '0006_auto_20190111_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='pVisit',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='state',
            field=models.CharField(max_length=255),
        ),
    ]
