from django.db import models

class Chart(models.Model):

    id = models.IntegerField(blank=False, null=False, primary_key=True, verbose_name='id-чата')