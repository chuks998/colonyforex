# Generated by Django 3.1.5 on 2021-08-18 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/profile/default.jpg', upload_to='profile'),
        ),
    ]
