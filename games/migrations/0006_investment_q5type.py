# Generated by Django 2.2.1 on 2019-10-31 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_auto_20191031_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='q5type',
            field=models.IntegerField(default=-1),
        ),
    ]
