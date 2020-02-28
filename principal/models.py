from django.contrib.gis.db import models


class TiposDeDatos(models.Model):
    # wsg 84
    punto_ws84 = models.PointField(srid=4326, blank=True, null=True)
    # peru
    punto = models.PointField(srid=32718, blank=True, null=True)
    multi_punto = models.MultiPointField(srid=32718, blank=True, null=True)
    poligono = models.PolygonField(srid=32718, blank=True, null=True)
    multi_poli = models.MultiPolygonField(srid=32718, blank=True, null=True)
    linea = models.LineStringField(srid=32718, blank=True, null=True)
    multi_linea = models.MultiLineStringField(srid=32718, blank=True, null=True)


class Imagenes(models.Model):
    foto = models.ImageField(upload_to='imagen')
