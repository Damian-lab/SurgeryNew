from pyexpat import model
from django.db import models

# Create your models here.


class Edliz(models.Model):
    name_of_drug = models.CharField(max_length=100,  blank=True)
   

    def __str__(self):
        # declaring an object
        return "name_of_drug-{}".format(self.name_of_drug)

    @classmethod
    def get_all_choices(cls):
        # I still suggest you to go through Django documentation
        # to understand what query sets are
        return cls.objects.values_list('name_of_drug', flat=True)

   