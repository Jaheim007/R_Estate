from django.contrib import admin
from Authentication import models

@admin.register(models.User)
class User(admin.ModelAdmin):
    list_display = (
        "username", 
        "first_name",
        "last_name", 
        "email",
        "image" , 
        "phone_number" , 
        "facebook",
        "instagram",
        "twitter",
        "linkedin", 
    )   