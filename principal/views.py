from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *


# Create your views here.
def index(request):
    return render(request, 'leaflet.html')




class TiposDatosViewset(viewsets.ModelViewSet):
    queryset = TiposDeDatos.objects.all()
    serializer_class = TposDeDatosSerializer
