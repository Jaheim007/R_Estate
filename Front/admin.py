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


# Register your models here.
