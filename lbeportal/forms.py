from django import forms
from datetime import datetime
from django.forms import ModelForm

from lbeportal.models import SiteVendor


class SiteVendorForm(ModelForm):
    class Meta:
        model = SiteVendor
        fields = '__all__'