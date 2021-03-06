# Generated by Django 3.1.5 on 2021-08-10 18:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_currency', models.CharField(max_length=9)),
                ('minor_currency', models.CharField(max_length=9)),
                ('Trend', models.CharField(choices=[('Buy', 'BUY'), ('Buy stop', 'BUY STOP'), ('Sell', 'SELL'), ('Sell Stop', 'SELL STOP')], default=1, max_length=9)),
                ('Take_profit', models.DecimalField(decimal_places=5, default=0.0, max_digits=9)),
                ('Stop_loss', models.DecimalField(decimal_places=5, default=0.0, max_digits=9)),
                ('Date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
