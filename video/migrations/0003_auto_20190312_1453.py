# Generated by Django 2.2b1 on 2019-03-12 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='Video_title',
            new_name='video_title',
        ),
    ]