from django.db import models
from django.utils.safestring import mark_safe


class LinkRandomMessage(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.URLField(blank=False, null=False, verbose_name='Ссылка')
    def __str__(self):
        return self.link
    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

class StickerRandomMessage(models.Model):
    id = models.AutoField(primary_key=True)
    sticker_image = models.ImageField(
        blank=False,
        null=False,
        max_length=255,
        verbose_name='Ссылка на стикер',
        help_text='Загрузите картинку стикера. Не будет нигде отображаться -- нужно только для админки'
    )
    sticker_id = models.CharField(
        blank=False,
        null=False,
        max_length=255,
        verbose_name='ID стикера',
        help_text='Чтобы узнать ID стикера, отправьте его этому https://t.me/idstickerbot боту'
    )
    def __str__(self):
        return mark_safe(f'<img src="{self.sticker_image.url}" style="height: 50px; width: auto;" />')

    class Meta:
        verbose_name = 'Стикер'
        verbose_name_plural = 'Стикеры'