# Generated by Django 4.2.7 on 2023-11-28 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lost',
            name='user',
        ),
    ]
