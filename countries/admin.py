from django.contrib import admin
from .models import Country, Institution


class CountryAdmin(admin.ModelAdmin):
    ordering = ['iso3']
    search_fields = ('name'),
    pass


class InstitutionAdmin(admin.ModelAdmin):
    autocomplete_fields = ['country']
    
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