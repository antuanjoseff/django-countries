from django.contrib import admin
from django.contrib.gis import admin as gisadmin
from tabbed_admin import TabbedModelAdmin

from .models import Country, Institution, Person, Mobility, MobilityCalendar, MobilityDone, User
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
            formfield.widget.can_view_related = False
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
        field.widget.can_view_related = False
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field.widget.can_delete_related = False

        return form

    # SKIP EDIT/ADD/VIEW BUTTONS IN INLINE FORM
    def formfield_for_dbfield(self, *args, **kwargs):
        formfield = super().formfield_for_dbfield(*args, **kwargs)
        if hasattr(formfield, "widget"):
            formfield.widget.can_view_related = False
            formfield.widget.can_add_related = False
            formfield.widget.can_delete_related = False
            formfield.widget.can_change_related = False
        else:
            pass  # this relation doesn't have an admin page to add/delete/change

        return formfield

def is_OI_member(user):
    return user.groups.filter(name='OI').exists()


class InstitutionAdmin(gisadmin.GISModelAdmin,  TabbedModelAdmin):
   
    def get_queryset(self, request):       
        qs = super().get_queryset(request)
        if is_OI_member(request.user):
            return qs
        return qs.filter(user=request.user)
    
    #Executed everytime an instance of Institution model is saved
    def save_model(self, request, obj, form, change):
        print(request.user)
        print('-'*40)
        print(request.user.username)
        if not obj.user:
            obj.user = request.user #user who created the object should only be set once
        # obj.updated_user = request.user #user that last updated the object can be set on each save
        super().save_model(request, obj, form, change)

    list_display = ('name', 'user')

    # DEFAULT TABS
    
    tab_solicitud = (
            (None, {
                'fields': ('benefits', 'name', 'geom', 'empowerment', 'collaboration_start')
            }),        
        )

    tab_mobilities = (
        (None, {
            'fields': ('motive',)
        }),        
        MobilityInline,
        MobilityCalendarInline,
        MobilityDoneInline,   
    )

    # TABS REQUIRED BEFORE THEY CAN BE OVERRIDE IN get_tabs
    tabs = [
        ('Detalls de la sol·licitud', tab_solicitud),
        ('Mobilitats sol·licitades', tab_mobilities),
    ]   

    # OVERRIDE TABS
    def get_tabs(self, request, obj=None):
        tabs = self.tabs

        tab_overview = (
                (None, {
                    'fields': ('country', )
                }),
            )

        if is_OI_member(request.user):
            tab_overview = (
                (None, {
                    'fields': ('country', 'region_ue', 'region_udg')
                }),
            )


        tabs = [
            ('Dades generals', tab_overview),
            ('Detalls de la sol·licitud', self.tab_solicitud),
            ('Mobilitats sol·licitades', self.tab_mobilities),
        ]   
        
        self.tabs = tabs
        return super(InstitutionAdmin, self).get_tabs(request, obj)

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

admin.site.register(User)
# admin.site.register(Mobility, MobilityAdmin)
# admin.site.register(MobilityCalendar)