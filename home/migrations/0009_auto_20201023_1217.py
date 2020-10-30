# Generated by Django 3.1.1 on 2020-10-23 06:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0008_auto_20201013_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upvote',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='user',
        ),
        migrations.AddField(
            model_name='wiki',
            name='thumbs',
            field=models.ManyToManyField(blank=True, default=None, related_name='thumbs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='wiki',
            name='thumbsdown',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='wiki',
            name='thumbsup',
            field=models.IntegerField(default='0'),
        ),
        migrations.DeleteModel(
            name='DownVote',
        ),
        migrations.DeleteModel(
            name='UpVote',
        ),
    ]
