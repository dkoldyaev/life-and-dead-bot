# Generated by Django 3.2.5 on 2021-09-02 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_alter_aboutbutton_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardbutton',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/cards/image', verbose_name='Изображение'),
        ),
    ]
