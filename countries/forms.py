from django import forms
from .models import Institution
from django.urls import reverse_lazy

class InstitutionAdminForm(forms.ModelForm):
    bbox = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = Institution
        fields = "__all__"

        htmx_attrs = {
            "hx-get": reverse_lazy("get_country_bbox"),
            "hx-swap": "outerHTML",
            "hx-trigger": "load,change",
            "hx-target": "#id_bbox",
        }        

        widgets = {
            "country": forms.Select(attrs=htmx_attrs),
        }
