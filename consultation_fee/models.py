from django.db import models

# Create your models here.


class ConsultationFee(models.Model):
    fee = models.IntegerField(blank=True)
   
   

    def __str__(self):
        # declaring an object
        return "consultation fee-{} ".format(self.fee)
