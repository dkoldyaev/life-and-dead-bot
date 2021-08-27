# Generated by Django 3.2.5 on 2021-08-21 23:33

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardButton',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('text', markdownx.models.MarkdownxField(blank=True, help_text='Для форматирование используйте <a href="https://core.telegram.org/api/entities" target="_blank">инструкции</a><br/>&lt;strong&gt;<strong>bold</strong>&lt;/strong&gt;, &lt;em&gt;<em>italic</em>&lt;/em&gt;, &lt;del&gt;<del>strike</del>&lt;/del&gt;', max_length=1024, null=True, verbose_name='Текст')),
                ('image', models.ImageField(upload_to='media/cards/image', verbose_name='Изображение')),
                ('button_text', models.CharField(max_length=50, verbose_name='Текст кнопки')),
                ('row', models.IntegerField(verbose_name='Номер ряда кнопки')),
                ('col', models.IntegerField(verbose_name='Порядок кнопки в ряду')),
            ],
            options={
                'verbose_name': 'Карточка',
                'verbose_name_plural': 'Карточки',
                'ordering': ['row', 'col'],
            },
        ),
        migrations.CreateModel(
            name='MainMenuButtons',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=255, verbose_name='Текст кнопки')),
                ('action', models.CharField(choices=[('get_link', 'Получить ссылку'), ('get_menu', 'Показать меню'), ('get_map', 'Показать карту')], max_length=255, verbose_name='Действие по кнопке')),
                ('row', models.IntegerField(default=1, verbose_name='Номер ряда кнопки')),
                ('col', models.IntegerField(default=1, verbose_name='Порядок кнопки в ряду')),
            ],
            options={
                'verbose_name': 'Элемент меню',
                'verbose_name_plural': 'Элементы меню',
                'ordering': ['row', 'col'],
            },
        ),
    ]
