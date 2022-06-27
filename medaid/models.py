from django.db import models

# Create your models here.


class MedAid(models.Model):
    threshold_amount = models.IntegerField(blank=True)
    medaid_name = models.CharField(max_length=200,blank=True)
   

    def __str__(self):
        # declaring an object
        return "threshold_amount-{} medaid_name-{} ".format(self.threshold_amount, self.medaid_name)
