# from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import  TiposDeDatos


class TposDeDatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiposDeDatos
        geo_field = ['punto', 'multi_punto', 'poligono', 'multi_poli', 'linea', 'multi_linea']
        fields = '__all__'
