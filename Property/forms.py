from django import forms
from django.forms import ModelForm

from Property import models

class AddProperty(ModelForm):
    class Meta:
        model = models.Properties
        fields = [
            'name', 
            'price',
            'status',
            'property_type',
            'bedroom',
            'bathroom',
            'garage',
            'address_name',
            'description',
            'main_image'
        ]