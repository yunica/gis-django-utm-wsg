from .models import TiposDeDatos
from django.contrib.gis import geos
import copy as cp


def create_poligon():
    geojson_coordinate = [
        [
            [
                585427.0793102034,
                8544195.80915265
            ],
            [
                585349.8118038538,
                8544232.438023267
            ],
            [
                585359.5218255294,
                8544252.978876641
            ],
            [
                585440.2042059419,
                8544233.9243908
            ],
            [
                585427.0793102034,
                8544195.80915265
            ]
        ]
    ]
    opoligon = geos.Polygon(geojson_coordinate[0], srid=32718)
    opoligon_wsg = cp.deepcopy(opoligon)
    opoligon_wsg.transform(4326)

    print(opoligon.area)
    otipos = TiposDeDatos(poligono=opoligon, punto_ws84=opoligon_wsg.centroid)
    otipos.save()
