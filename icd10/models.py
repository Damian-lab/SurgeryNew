from pyexpat import model
from django.db import models

# Create your models here.


class Icd10(models.Model):
    chapter_description = models.CharField(max_length=100,  blank=True)
    group_code = models.CharField(max_length=100,  blank=True)
    group_description = models.CharField(max_length=100, blank=True)
    icd10_3_code = models.CharField(max_length=100, blank=True)
    icd10_3_code_description =models.CharField(max_length=500,  blank=True)
    icd10_code= models.CharField(max_length=100,  blank=True)
    who_full_description = models.CharField(max_length=100,  blank=True)

    def __str__(self):
        # declaring an object
        return "chapter_description-{} group_code-{} group_description-{} icd10_3_code-{} icd10_3_code_description-{} icd10_code-{} who_full_description-{}".format(self.chapter_description, self.group_code, self.group_description, self.icd10_3_code, self.icd10_3_code_description, self.icd10_code, self.who_full_description)

    @classmethod
    def get_all_choices(cls):
        # I still suggest you to go through Django documentation
        # to understand what query sets are
        return cls.objects.values_list('icd10_code', flat=True)