from django.contrib import admin
from .models import *
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

admin.site.register(TiposDeDatos,LeafletGeoAdmin)
admin.site.register(Imagenes)
