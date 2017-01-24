from rest_framework import serializers

from bullet.items.models import Item, ItemSignifierRelationship


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
            'url'
        )


class ItemSignifierRelationshipSerializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = ItemSignifierRelationship
        fields = '__all__'