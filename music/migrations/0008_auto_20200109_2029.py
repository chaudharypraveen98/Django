# Generated by Django 2.1.5 on 2020-01-09 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20200109_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_logo',
            field=models.FileField(max_length=140, null=True, upload_to=''),
        ),
    ]
