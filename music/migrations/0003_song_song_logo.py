# Generated by Django 2.1.5 on 2019-07-25 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_logo',
            field=models.CharField(default=1, max_length=1250),
            preserve_default=False,
        ),
    ]
