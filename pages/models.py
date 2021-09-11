from django.db import models
from markdownx.models import MarkdownxField


class Page(models.Model):
    command = models.CharField(
        blank=False,
        null=False,
        max_length=255,
        db_index=True,
        choices=(
            ('start', '/start'),
            ('help', '/help'),
            ('map', 'Кнопка карты'),
            ('about', 'О выставке'),
            ('menu', 'Кнопка меню'),
            ('error', 'Сообщение об ошибке'),
        ),
        primary_key=True
    )
    title = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        verbose_name='Заголовок',
        help_text='Не будет нигде отображаться, '
                  'используется только для того, чтобы понимать, что за страница'
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
        blank=True,
        null=True,
        upload_to='pages/page/image',
        verbose_name='Изображение'
    )

    def __str__(self):
        return f'{self.command} - {self.title}'

    class Meta:
        verbose_name = 'Статичное сообщение'
        verbose_name_plural = 'Статичные сообщения'
        ordering = ''