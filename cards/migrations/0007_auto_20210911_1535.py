# Generated by Django 3.2.5 on 2021-09-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_alter_cardbutton_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutbutton',
            name='col',
            field=models.IntegerField(db_index=True, verbose_name='Порядок кнопки в ряду'),
        ),
        migrations.AlterField(
            model_name='aboutbutton',
            name='row',
            field=models.IntegerField(db_index=True, verbose_name='Номер ряда кнопки'),
        ),
        migrations.AlterField(
            model_name='cardbutton',
            name='col',
            field=models.IntegerField(db_index=True, verbose_name='Порядок кнопки в ряду'),
        ),
        migrations.AlterField(
            model_name='cardbutton',
            name='row',
            field=models.IntegerField(db_index=True, verbose_name='Номер ряда кнопки'),
        ),
        migrations.AlterField(
            model_name='mainmenubuttons',
            name='col',
            field=models.IntegerField(db_index=True, default=1, verbose_name='Порядок кнопки в ряду'),
        ),
        migrations.AlterField(
            model_name='mainmenubuttons',
            name='row',
            field=models.IntegerField(db_index=True, default=1, verbose_name='Номер ряда кнопки'),
        ),
    ]
