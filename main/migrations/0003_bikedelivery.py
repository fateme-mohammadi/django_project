# Generated by Django 5.0 on 2024-01-30 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_food_food_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeDelivery',
            fields=[
                ('bikedelivery_code', models.IntegerField(primary_key=True, serialize=False)),
                ('bikedelivery_name', models.CharField(max_length=50)),
            ],
        ),
    ]
