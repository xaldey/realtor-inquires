from django.contrib import admin

from .models import Contact, Lead


class LeadAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "contact_tstamp")
    list_display_links = ("id", "name")
    search_fields = ("name", "email")
    list_per_page = 25


class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "email", "contact_date")
    list_display_links = ("id", "last_name")
    search_fields = ("last_name", "email")
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
admin.site.register(Lead, LeadAdmin)
