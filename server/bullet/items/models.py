# coding=utf-8
from django.db import models

from bullet.signifiers.models import Signifier
from utils import Choice


class ItemType(Choice):
    TASK = 'task'
    EVNT = 'event'
    NOTE = 'note'


class Item(models.Model):
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=2 ** 14)
    type = models.CharField(max_length=4, choices=ItemType.choices())
    signifiers = models.ManyToManyField(
        Signifier,
        through='ItemSignifierRelationship'
    )
    complete = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=True)

    def __unicode__(self):
        return 'Bullet item {}: {}'.format(
            self.id, self.title
        )


class ItemSignifierRelationship(models.Model):
    signifier = models.ForeignKey(Signifier)
    item = models.ForeignKey(Item)

    class Meta:
        unique_together = [
            ['signifier', 'item'],
        ]

    def __unicode__(self):
        return '{} signifier on item {}'. format(
            self.signifier, self.item
        )
