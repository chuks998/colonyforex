# Generated by Django 3.1.5 on 2021-08-17 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Hello i am new to Colony', max_length=200),
        ),
    ]
