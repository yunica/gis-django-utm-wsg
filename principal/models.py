from django.contrib.gis.db import models


class TiposDeDatos(models.Model):
    # wsg 84
    punto_ws84 = models.PointField(srid=4326)
    # peru
    punto = models.PointField(srid=32718)
    multi_punto = models.MultiPointField(srid=32718)
    poligono = models.PolygonField(srid=32718)
    multi_poli = models.MultiPolygonField(srid=32718)
    linea = models.LineStringField(srid=32718)
    multi_linea = models.MultiLineStringField(srid=32718)


class Imagenes(models.Model):
    foto = models.ImageField(upload_to='imagen')

