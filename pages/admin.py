from django.contrib import admin

from pages.models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass