# Generated by Django 2.2.16 on 2020-10-21 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movieinfo',
            old_name='genre',
            new_name='genres',
        ),
    ]
