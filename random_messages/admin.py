from django.contrib import admin
from django.utils.safestring import mark_safe

from random_messages.models import LinkRandomMessage, StickerRandomMessage


@admin.register(LinkRandomMessage)
class LinkRandomMessageAdmin(admin.ModelAdmin):
    pass

@admin.register(StickerRandomMessage)
class StickerRandomMessageAdmin(admin.ModelAdmin):
    list_display = ['sticker_preview', 'sticker_image', 'sticker_id']
    list_editable = ['sticker_image', 'sticker_id']
    list_display_links = ['sticker_preview']
    readonly_fields = ['sticker_preview']
    fieldsets = [
        (
            None, {
                'fields': ['sticker_preview']
            }
        ),
        (
            None, {
                'fields': ['sticker_image', 'sticker_id']
            }
        ),
    ]
    def sticker_preview(self, obj):
        try:
            return mark_safe(f'<img src="{obj.sticker_image.url}" />')
        except:
            return 'Нет изображения'