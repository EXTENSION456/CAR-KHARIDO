# Generated by Django 2.2.1 on 2019-11-29 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20191129_1107'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='bookcars',
            new_name='rentcars',
        ),
    ]
