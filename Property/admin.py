from django.contrib import admin

from Property import models


@admin.register(models.Bathrooms)
class Bathrooms(admin.ModelAdmin):
    list_display = (
        'number',
    )
    
@admin.register(models.Bedrooms)
class Bedrooms(admin.ModelAdmin):
    list_display = (
        'number',
    )
    
@admin.register(models.Garages)
class Garages(admin.ModelAdmin):
    list_display = (
        'number',
    )

@admin.register(models.TypeProperty)
class TypeProperty(admin.ModelAdmin):
    list_display = (
        'property_type',
    )
    
@admin.register(models.Cities)
class Cities(admin.ModelAdmin):
    list_display = (
        'city',
    )

@admin.register(models.Properties)
class Properties(admin.ModelAdmin):
    list_display = (
        'name', 
        'price',
        'status',
        'bedroom',
        'bathroom',
        'garage',
        'description',
        'property_type',
        'address_name',
        'location',
        'main_image',
        'users' 
    )

@admin.register(models.RequestTime)
class Request(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "subject",
        "message",
        'save_user'

    )