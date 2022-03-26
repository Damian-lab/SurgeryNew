from django.db import models

# Create your models here.


class PaymentMethod(models.Model):
    rate = models.IntegerField(blank=True)
    currency_name = models.CharField(max_length=200,blank=True)
   

    def __str__(self):
        # declaring an object
        return "rate-{} currency_name-{} ".format(self.rate, self.currency_name)
