from django.contrib import admin
from personas.models import Domicilio
from personas.models import Persona

# Register your models here.
admin.site.register(Persona)
admin.site.register(Domicilio)