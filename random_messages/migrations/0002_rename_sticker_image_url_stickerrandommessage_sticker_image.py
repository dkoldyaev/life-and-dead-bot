# Generated by Django 3.2.5 on 2021-08-29 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('random_messages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stickerrandommessage',
            old_name='sticker_image_url',
            new_name='sticker_image',
        ),
    ]
