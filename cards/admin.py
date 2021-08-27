from django.contrib import admin
from django.utils.safestring import mark_safe
from markdownx.admin import MarkdownxModelAdmin
from django.conf import settings

from cards.models import CardButton, MainMenuButtons

@admin.register(CardButton)
class CardButtonAdmin(MarkdownxModelAdmin):
    list_display = ['list_link', 'button_text', 'image', 'image_preview', 'row', 'col']
    list_editable = ['button_text', 'image', 'row', 'col']
    list_display_links = ['list_link']
    readonly_fields = ['list_link', 'image_preview']
    fieldsets = [
        (
            None, {
                'fields': ['title', 'button_text', 'row', 'col']
            }
        ),
        (
            None, {
                'fields': ['text', 'image', 'image_preview']
            }
        ),
    ]
    def list_link(self, obj: CardButton):
        return obj.title or obj.button_text
    def image_preview(self, obj: CardButton):
        return mark_safe(f'<img src="{obj.image.url}" style="width: 200px; height: auto" />')

@admin.register(MainMenuButtons)
class MainMenuAdmin(admin.ModelAdmin):
    list_display = ['list_link', 'text', 'action', 'row', 'col']
    list_editable = ['text', 'action', 'row', 'col']
    list_display_links = ['list_link']
    readonly_fields = ['list_link']
    def list_link(self, obj: MainMenuButtons):
        return obj.text