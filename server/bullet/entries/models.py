from django.db import models

from bullet.items.models import Item
from bullet.utils import Choice


class PageType(Choice):
    FUT = 'future'
    MON = 'monthly'
    WEE = 'weekly'
    DAI = 'daily'
    COL = 'collection'


class EntryState(Choice):
    POS = 'postponed'
    SCH = 'scheduled'


class Entry(models.Model):
    item = models.ForeignKey(Item, related_name='entries')
    state = models.CharField(max_length=3, choices=EntryState.choices())
    date = models.DateField()
    creation_date = models.DateTimeField(auto_now=True)
    page_type = models.CharField(max_length=3, choices=PageType.choices())

    def __str__(self):
        return "{} {} entry for '{}' ".format(
            getattr(PageType, self.page_type).value.capitalize(),
            getattr(EntryState, self.state).value,
            self.item
        )




