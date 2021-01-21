from django.db import models

# Create your models here.
class PaymentModel(models.Model):
    cardNumber = models.CharField(max_length=16)
    cardName = models.CharField(max_length=1000)
    secNumber  =models.CharField(max_length=3)
    expiry = models.DateField(blank=True)
    amount = models.DecimalField( max_digits=5, decimal_places=2)
    

    def __str__(self):
        return self.cardName



