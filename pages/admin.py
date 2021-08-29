from django.contrib import admin
from django.utils.safestring import mark_safe

from pages.models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['command', 'title', 'text', 'image_preview', 'image']
    list_display_links = ['command']
    list_editable = ['title', 'text', 'image']
    readonly_fields = ['image_preview']
    fieldsets = [
        (
            None, {
                'fields': ['command', 'title']
            },
        ),
        (
            None, {
                'fields': ['text', 'image_preview', 'image']
            }
        )
    ]
    def image_preview(self, obj):
        if not obj.image.url :
            return 'Нет изображения'
        return mark_safe(
            f'<img src="{obj.image.url}" style="width: 250px; height: auto;" />'
        )