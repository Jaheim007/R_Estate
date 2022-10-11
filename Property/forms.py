from django import forms
from django.forms import ModelForm

from Property import models

class AddPropertyForm(ModelForm):
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
            'main_image',
            'description',
            'additional_image1',
            'additional_image2',
            'additional_image3',
            
        ]