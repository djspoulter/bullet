from rest_framework import serializers

from bullet.signifiers.models import Signifier


class SignifierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Signifier
        fields = '__all__'
