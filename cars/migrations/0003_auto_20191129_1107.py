# Generated by Django 2.2.1 on 2019-11-29 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_bookcars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcars',
            name='Request_date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='bookcars',
            name='Return_date',
            field=models.CharField(max_length=50),
        ),
    ]