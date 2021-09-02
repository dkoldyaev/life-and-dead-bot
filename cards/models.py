from django.db import models
from markdownx.models import MarkdownxField


class CardButton(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        verbose_name='Заголовок'
    )
    text = MarkdownxField(
        blank=True,
        null=True,
        verbose_name='Текст',
        max_length=1024,
        help_text='Для форматирование используйте '
                  '<a href="https://core.telegram.org/api/entities" target="_blank">инструкции</a>'
                  '<br/>'
                  '&lt;strong&gt;<strong>bold</strong>&lt;/strong&gt;, &lt;em&gt;<em>italic</em>&lt;/em&gt;, &lt;del&gt;<del>strike</del>&lt;/del&gt;'
    )
    image = models.ImageField(
        blank=False,
        null=False,
        upload_to='media/cards/image',
        verbose_name='Изображение'
    )

    button_text = models.CharField(blank=False, null=False, max_length=50, verbose_name='Текст кнопки')
    row = models.IntegerField(blank=False, null=False, verbose_name='Номер ряда кнопки')
    col = models.IntegerField(blank=False, null=False, verbose_name='Порядок кнопки в ряду')

    def __str__(self):
        return f'-{self.row}-{self.col}-{self.button_text}'

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
        ordering = ['row', 'col']

class AboutButton(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        verbose_name='Заголовок'
    )
    text = MarkdownxField(
        blank=True,
        null=True,
        verbose_name='Текст',
        max_length=1024,
        help_text='Для форматирование используйте '
                  '<a href="https://core.telegram.org/api/entities" target="_blank">инструкции</a>'
                  '<br/>'
                  '&lt;strong&gt;<strong>bold</strong>&lt;/strong&gt;, &lt;em&gt;<em>italic</em>&lt;/em&gt;, &lt;del&gt;<del>strike</del>&lt;/del&gt;'
    )
    image = models.ImageField(
        blank=False,
        null=False,
        upload_to='media/about/image',
        verbose_name='Изображение'
    )

    button_text = models.CharField(blank=False, null=False, max_length=50, verbose_name='Текст кнопки')
    row = models.IntegerField(blank=False, null=False, verbose_name='Номер ряда кнопки')
    col = models.IntegerField(blank=False, null=False, verbose_name='Порядок кнопки в ряду')

    def __str__(self):
        return f'-{self.row}-{self.col}-{self.button_text}'

    class Meta:
        verbose_name = 'Карточка "о выставке"'
        verbose_name_plural = 'Карточки "о выставке"'
        ordering = ['row', 'col']

class MainMenuButtons(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(
        blank=False,
        null=False,
        max_length=255,
        verbose_name='Текст кнопки'
    )
    action = models.CharField(
        null=False,
        blank=False,
        max_length=255,
        verbose_name='Действие по кнопке',
        choices=[
            ('get_link', 'Получить ссылку'),
            ('get_menu', 'Показать меню'),
            ('get_map', 'Показать карту'),
            ('get_about', 'О выставке')
        ]
    )
    row = models.IntegerField(blank=False, null=False, verbose_name='Номер ряда кнопки', default=1)
    col = models.IntegerField(blank=False, null=False, verbose_name='Порядок кнопки в ряду', default=1)

    def __str__(self):
        return f'-{self.row}-{self.col}-{self.text}'

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'
        ordering = ['row', 'col']
