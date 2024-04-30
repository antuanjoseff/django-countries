from django.contrib import admin
from django.contrib.gis import admin as gisadmin
from .models import Country, Institution
from .widgets import CustomGeoWidget


class CountryAdmin(admin.ModelAdmin):
    ordering = ['iso3']
    search_fields = ('name'),
    pass


class InstitutionAdmin(gisadmin.GISModelAdmin):
    autocomplete_fields = ['country']
    gis_widget = CustomGeoWidget

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


admin.site.register(Country, CountryAdmin)
admin.site.register(Institution, InstitutionAdmin)