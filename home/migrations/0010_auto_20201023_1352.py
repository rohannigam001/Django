# Generated by Django 3.1.1 on 2020-10-23 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20201023_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wiki',
            name='thumbs',
        ),
        migrations.RemoveField(
            model_name='wiki',
            name='thumbsdown',
        ),
        migrations.RemoveField(
            model_name='wiki',
            name='thumbsup',
        ),
    ]