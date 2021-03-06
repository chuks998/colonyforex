# Generated by Django 3.1.5 on 2021-08-10 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0002_auto_20210810_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signal',
            old_name='Stop_loss',
            new_name='entry',
        ),
        migrations.RenameField(
            model_name='signal',
            old_name='Take_profit',
            new_name='stop_loss',
        ),
        migrations.RenameField(
            model_name='signal',
            old_name='Trend',
            new_name='trend',
        ),
        migrations.AddField(
            model_name='signal',
            name='take_profit',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=9),
        ),
    ]
