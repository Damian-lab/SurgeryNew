from import_export import resources
from .models import Icd10

class Icd10Resource(resources.ModelResource):
    class meta:
        model = Icd10
