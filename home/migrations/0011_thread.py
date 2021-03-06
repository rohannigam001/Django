# Generated by Django 3.1.1 on 2020-10-23 15:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0010_auto_20201023_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userDownVotes', models.ManyToManyField(blank=True, related_name='threadDownVotes', to=settings.AUTH_USER_MODEL)),
                ('userUpVotes', models.ManyToManyField(blank=True, related_name='threadUpVotes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
