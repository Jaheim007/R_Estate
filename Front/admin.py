from django.contrib import admin

from Front import models

@admin.register(models.Contact)
class Contact(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "subject",
        "message"
    )

@admin.register(models.Newsletters)
class Newsletter(admin.ModelAdmin):
    list_display = (
        "email",
    )
    


# Register your models here.
