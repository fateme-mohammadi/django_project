# Generated by Django 5.0.1 on 2024-01-27 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='food_image',
            field=models.ImageField(default='default.png', upload_to='food_images/'),
        ),
    ]
