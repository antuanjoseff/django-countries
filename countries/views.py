from django.http import JsonResponse
from django.shortcuts import render
from .models import Country
from django.core.exceptions import PermissionDenied
from django.contrib.gis.db.models.functions import AsGeoJSON
from django.contrib.gis.geos import Point


def get_country_bbox(request):
    if request.user.is_authenticated:
        iso3 = request.GET.get('country', '')
        qs = Country.objects.values('bbox').annotate(geojson=AsGeoJSON("geom")).filter(pk=iso3)      

        return JsonResponse(list(qs), safe=False)
    
    else: 
        raise PermissionDenied()


def get_country_from_point(request):
    if request.user.is_authenticated:
        print('authenticated')
        try:
            lat = request.GET.get('lat', 0)
            lng = request.GET.get('lng', 0)
            pnt = Point(float(lat), float(lng), srid=4326)

            qs = Country.objects.values('iso3', 'name').filter(geom__contains=pnt)
        except:
            raise PermissionDenied()
        
        if len(qs):
            return JsonResponse(list(qs), safe=False)
        else:
            return JsonResponse([{'iso3':''}],safe=False, status=200)
        
    else:
        raise PermissionDenied()