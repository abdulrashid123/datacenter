# Generated by Django 2.2b1 on 2019-04-17 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0004_auto_20190417_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='values',
            name='parameter',
        ),
        migrations.AddField(
            model_name='values',
            name='parameter_name',
            field=models.ManyToManyField(to='table.Parameter'),
        ),
    ]
