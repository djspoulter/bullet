from rest_framework import serializers

from bullet.items.models import Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = (
            'title',
            'body',
            'complete',
            'cancelled',
            'type',
            'signifiers',
        )
