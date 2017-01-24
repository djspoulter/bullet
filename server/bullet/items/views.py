# Create your views here.
from rest_framework.viewsets import ModelViewSet

from bullet.items.models import Item
from bullet.items.serialisers import ItemSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
