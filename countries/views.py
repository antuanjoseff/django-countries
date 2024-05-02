from django.http import JsonResponse
from django.shortcuts import render
from .models import Country
from django.core.exceptions import PermissionDenied
from django.contrib.gis.db.models.functions import AsGeoJSON


def get_country_bbox(request):
    if request.user.is_authenticated:
        iso3 = request.GET.get('country', '')
        qs = Country.objects.values('bbox').annotate(geojson=AsGeoJSON("geom")).filter(pk=iso3)      

        return JsonResponse(list(qs), safe=False)
    
    else: 
        raise PermissionDenied()