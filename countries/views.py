from django.shortcuts import render
from .models import Country

def get_country_bbox(request):
    coto_id = request.GET.get('country', '')
    bbox = Country.objects.filter(pk=coto_id).values_list('bbox').first()

    return HttpResponse("""
        <input type="text" name="bbox" required="" id="id_bbox" value="{}">
        <script>
           changeMapView()
        </script>
    """.format(bbox))