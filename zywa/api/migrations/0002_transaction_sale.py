# Generated by Django 4.0.8 on 2023-12-11 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='sale',
            field=models.FloatField(null=True),
        ),
    ]
