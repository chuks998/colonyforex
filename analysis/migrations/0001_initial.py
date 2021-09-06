# Generated by Django 3.1.5 on 2021-08-16 19:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.TimeField(default=datetime.datetime(2021, 8, 16, 19, 9, 16, 403885, tzinfo=utc))),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads', verbose_name='image')),
                ('post_title', models.CharField(blank=True, max_length=200, null=True)),
                ('post_subject', models.CharField(blank=True, max_length=500, null=True)),
                ('post_body', models.CharField(blank=True, max_length=2200, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
