# Create your views here.
from rest_framework.viewsets import ModelViewSet

from bullet.items.models import Item, ItemSignifierRelationship
from bullet.items.serialisers import ItemSerializer, \
    ItemSignifierRelationshipSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemSignifierRelationshipViewSet(ModelViewSet):
    queryset = ItemSignifierRelationship.objects.all()
    serializer_class = ItemSignifierRelationshipSerializer
