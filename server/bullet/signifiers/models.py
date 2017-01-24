from django.db import models


class Signifier(models.Model):
    name = models.CharField(max_length=24)
    description = models.CharField(max_length=256)
    icon = models.CharField(max_length=20)
