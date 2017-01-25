from rest_framework.viewsets import ModelViewSet

from bullet.entries.models import Entry
from bullet.entries.serialisers import EntrySerializer


class EntryViewSet(ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
