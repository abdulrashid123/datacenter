# Generated by Django 2.2b1 on 2019-04-24 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0007_auto_20190417_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='unit',
            field=models.TextField(blank=True, null=True),
        ),
    ]