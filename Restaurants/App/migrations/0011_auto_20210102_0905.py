# Generated by Django 3.0.8 on 2021-01-02 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_auto_20210102_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantsmodel',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
