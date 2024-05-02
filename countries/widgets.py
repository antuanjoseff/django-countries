from django.contrib.gis.forms.widgets import BaseGeometryWidget

class CustomGeoWidget(BaseGeometryWidget):
    template_name = 'gis/custom_layers.html'
    map_srid = 3857
    default_lon = 0
    default_lat = 0
    default_zoom = 1
    map_width = 800
    map_height = 600
    
    class Media:
        css = {
            "all": (
                "https://cdn.jsdelivr.net/npm/ol@v7.2.2/ol.css",
                "gis/css/ol3.css",
            )
        }
        js = (
            "https://cdn.jsdelivr.net/npm/ol@v7.2.2/dist/ol.js",
            "gis/js/OLMapWidget.js",
        )

    def serialize(self, value):
        return value.json if value else ""

    def deserialize(self, value):
        geom = super().deserialize(value)
        # GeoJSON assumes WGS84 (4326). Use the map's SRID instead.
        if geom and self.map_srid != 4326:
            geom.srid = self.map_srid
        return geom

    def __init__(self, attrs=None):
        super().__init__()
        for key in ("default_lon", "default_lat", "default_zoom"):
            self.attrs[key] = getattr(self, key)
            
        if attrs:
            self.attrs.update(attrs)
