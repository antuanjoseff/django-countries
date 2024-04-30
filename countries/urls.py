from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("get_country_bbox/", views.get_country_bbox, name="get_country_bbox"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)