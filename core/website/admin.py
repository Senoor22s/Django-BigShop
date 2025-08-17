from django.contrib import admin
from .models import Newsletter,Contact


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ("name","phone_number","email", "created_date")
    list_filter = ("email",)
    search_fields = ["name", "message"]

admin.site.register(Newsletter)
admin.site.register(Contact, ContactAdmin)