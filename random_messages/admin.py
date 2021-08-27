from django.contrib import admin
from random_messages.models import LinkRandomMessage, StickerRandomMessage


@admin.register(LinkRandomMessage)
class LinkRandomMessageAdmin(admin.ModelAdmin):
    pass

@admin.register(StickerRandomMessage)
class StickerRandomMessageAdmin(admin.ModelAdmin):
    pass