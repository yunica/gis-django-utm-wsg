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


"""

pnt = GEOSGeometry('SRID=32718;POINT({} {})'.format(str(585274.0960410312),str(8544278.898776622)))
pnt.transform(4326)
pnt
<Point object at 0x7fbd9360d098>
pnt.x
-74.21313196420671
pnt.center
for change 
"""