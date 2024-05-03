from django.contrib import admin
from django.contrib.gis import admin as gisadmin
from tabbed_admin import TabbedModelAdmin

from .models import Country, Institution, Person, Mobility, MobilityCalendar, MobilityDone
from .widgets import CustomGeoWidget
from .forms import InstitutionAdminForm
from django import forms
from django.urls import reverse_lazy


class CountryAdmin(admin.ModelAdmin):
    ordering = ['iso3']
    search_fields = ('name'),
    pass


class MobilityInline(admin.TabularInline):
    model = Mobility
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(MobilityInline, self).get_form(request, obj, **kwargs)
    #     field = form.base_fields["type"]
    #     field.widget.can_view_related = False
    #     field.widget.can_add_related = False
    #     field.widget.can_change_related = False
    #     field.widget.can_delete_related = False

    #     return form

class MobilityDoneInline(admin.TabularInline):
    model = MobilityDone

class MobilityCalendarInline(admin.TabularInline):
    model = MobilityCalendar


class InstitutionAdmin(gisadmin.GISModelAdmin,  TabbedModelAdmin):

    tab_overview = (
        (None, {
            'fields': ('country', 'region_ue', 'region_udg')
        }),
    )

    tab_solicitud = (
        (None, {
            'fields': ('benefits', 'name', 'geom', 'empowerment', 'collaboration_start')
        }),        
    )

    tab_mobilities = (
        MobilityInline,
        MobilityCalendarInline,
        MobilityDoneInline,
        (None, {
            'fields': ('motive',)
        }),        
    )

    tabs = [
        ('Dades generals', tab_overview),
        ('Detalls de la sol·licitud', tab_solicitud),
        ('Mobilitats sol·licitades', tab_mobilities),
    ]
    gis_widget = CustomGeoWidget
    form = InstitutionAdminForm
    # autocomplete_fields = ['country']
    inlines = [
        MobilityInline, MobilityCalendarInline, MobilityDoneInline
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super(InstitutionAdmin, self).get_form(request, obj, **kwargs)
        field = form.base_fields["country"]
        field.widget.can_view_related = False
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field.widget.can_delete_related = False

        return form

    class Meta:
        verbose_name = 'Institució'
        verbose_name_plural = 'Institucions'


    class Media:
         js = ["admin/js/institutions.js"]



admin.site.register(Country, CountryAdmin)
admin.site.register(Institution, InstitutionAdmin)

admin.site.register(Person)
# admin.site.register(Mobility)
# admin.site.register(MobilityCalendar)