from rest_framework.viewsets import ModelViewSet

from bullet.signifiers.models import Signifier
from bullet.signifiers.serialisers import SignifierSerializer


class SignifierViewSet(ModelViewSet):
    queryset = Signifier.objects.all()
    serializer_class = SignifierSerializer
