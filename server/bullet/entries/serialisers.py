from rest_framework import serializers

from bullet.entries.models import Entry


class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        fields = (
            'item',
            'state',
            'date',
            'creation_date',
            'page_type',
            'url'
        )
