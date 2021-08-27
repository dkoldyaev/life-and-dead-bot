from django.db import models

class BotData(models.Model):
    id = models.AutoField(primary_key=True)
    host = models.URLField(blank=False, null=False, verbose_name='Домен для бота')
    token = models.CharField(blank=False, null=False, max_length=255, verbose_name='токен')

    class Meta:
        verbose_name = 'Данные бота'
        verbose_name_plural = 'Данные бота'