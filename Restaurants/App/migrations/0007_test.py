# Generated by Django 3.0.8 on 2021-01-02 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20201231_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('alternate', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
    ]
