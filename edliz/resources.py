from import_export import resources
from .models import Edliz

class EdlizResource(resources.ModelResource):
    class meta:
        model = Edliz
