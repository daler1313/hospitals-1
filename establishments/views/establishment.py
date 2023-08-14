from django.shortcuts import render
from rest_framework import generics


from ..models import Establishment
from ..serializer import EstablishmentSerializer


# Create your views here.
class EstablishmentList(generics.ListCreateAPIView):
  queryset = Establishment.objects.all()
  serializer_class = EstablishmentSerializer


class EstablishmentDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Establishment.objects.all()
  serializer_class = EstablishmentSerializer


class EstablishmentSearchByName(generics.ListAPIView):
    serializer_class = EstablishmentSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Establishment.objects.filter(name=name)


class EstablishmentSearchByCategory(generics.ListAPIView):
    serializer_class = EstablishmentSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Establishment.objects.filter(category=category)


class EstablishmentSearchByAddress(generics.ListAPIView):
    serializer_class = EstablishmentSerializer

    def get_queryset(self):
        address = self.kwargs['address']
        return Establishment.objects.filter(address=address)


