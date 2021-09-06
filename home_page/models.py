from django.db import models
from django.utils import timezone


class Signal(models.Model):
    TREND_CHOICE = (
        ('Buy','BUY'),
        ('Buy stop','BUY STOP'),
        ('Sell','SELL'),
        ('Sell Stop','SELL STOP'),
    )

    # currency pair fields...
    base_currency = models.CharField(max_length=9)
    minor_currency = models.CharField(max_length=9)

    # results fields
    trend = models.CharField(max_length=9, choices=TREND_CHOICE, default=1)
    entry = models.DecimalField(max_digits=9, decimal_places=5, default=0.000)
    take_profit = models.DecimalField(max_digits=9, decimal_places=5, default=0.000)
    stop_loss = models.DecimalField(max_digits=9, decimal_places=5, default=0.000)
    date_posted    = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.base_currency) + str(self.minor_currency ) +str('') + str(self.date_posted)