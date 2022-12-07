from django.contrib import admin
from .models import Developer


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_working", "is_holding_member")
    list_display_links = ("id", "name")
    list_editable = ("is_working", "is_holding_member")
    search_fields = ("name",)
    list_per_page = 25


admin.site.register(Developer, DeveloperAdmin)
