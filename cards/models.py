from django.db import models


class Cards(models.Model):

    STATUS = [
    ('ACTIVATED', 'ACTIVATED'),
    ('NOT ACTIVATED', 'NOT ACTIVATED'),
    ('EXPIRED', 'EXPIRED'),    
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    card_series = models.PositiveIntegerField()
    number_card = models.CharField(max_length=16)
    amount = models.DecimalField(max_digits=4, decimal_places=2)
    data_created = models.DateTimeField(auto_now_add=True)
    data_end = models.DateTimeField()    
    status = models.CharField(choices=STATUS, default='ACTIVATED', max_length=100)

    def __str__(self):
        return f'Серия Карты {self.card_series}: {self.first_name} {self.last_name}'

    