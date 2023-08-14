from rest_framework import serializers
from ..models import Establishment


class EstablishmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Establishment
    fields = ('id',"name","description","address","city","category","contact")