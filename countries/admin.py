from django.contrib import admin
from django.contrib.gis import admin as gisadmin
from tabbed_admin import TabbedModelAdmin

from .models import Country, Institution, Person, Mobility, MobilityCalendar, MobilityDone, MyUser
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
    extra = 1
        
    # SKIP EDIT/ADD/VIEW BUTTONS IN INLINE FORM
    def formfield_for_dbfield(self, *args, **kwargs):
        formfield = super().formfield_for_dbfield(*args, **kwargs)
        if hasattr(formfield, "widget"):
            formfield.widget.can_add_related = False
            formfield.widget.can_delete_related = False
            formfield.widget.can_change_related = False
        else:
            pass  # this relation doesn't have an admin page to add/delete/change

        return formfield
    
class MobilityDoneInline(admin.TabularInline):
    model = MobilityDone
    extra = 1

class MobilityCalendarInline(admin.TabularInline):
    model = MobilityCalendar
    extra = 1

    def get_form(self, request, obj=None, **kwargs):
        form = super(MobilityCalendarInline, self).get_form(request, obj, **kwargs)
        field = form.base_fields["type"]
        print(field)
        field.widget.can_view_related = False
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field.widget.can_delete_related = False

        return form

    # SKIP EDIT/ADD/VIEW BUTTONS IN INLINE FORM
    def formfield_for_dbfield(self, *args, **kwargs):
        formfield = super().formfield_for_dbfield(*args, **kwargs)
        if hasattr(formfield, "widget"):
            formfield.widget.can_add_related = False
            formfield.widget.can_delete_related = False
            formfield.widget.can_change_related = False
        else:
            pass  # this relation doesn't have an admin page to add/delete/change

        return formfield

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
    autocomplete_fields = ['country']
    inlines = [
        MobilityInline, MobilityCalendarInline, MobilityDoneInline
    ]

    class Meta:
        verbose_name = 'Institució'
        verbose_name_plural = 'Institucions'


    class Media:
         js = ["admin/js/institutions.js"]


admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Person)
admin.site.register(Country, CountryAdmin)

admin.site.register(MyUser)
# admin.site.register(Mobility, MobilityAdmin)
# admin.site.register(MobilityCalendar)