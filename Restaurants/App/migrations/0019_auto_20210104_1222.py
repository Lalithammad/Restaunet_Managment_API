# Generated by Django 3.0.8 on 2021-01-04 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0018_remove_restaurantsmodel_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantsmodel',
            name='total_tables',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookingmodel',
            name='tableNumber',
            field=models.CharField(max_length=5),
        ),
    ]
