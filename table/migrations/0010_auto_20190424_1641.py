# Generated by Django 2.2b1 on 2019-04-24 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0009_auto_20190424_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
