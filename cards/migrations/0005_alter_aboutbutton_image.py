# Generated by Django 3.2.5 on 2021-09-02 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_alter_cardbutton_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutbutton',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/about/image', verbose_name='Изображение'),
        ),
    ]
