from django.shortcuts import render
from rest_framework import generics


from ..models import Hospital
from ..serializer import HospitalSerializer


# Create your views here.
class HospitalList(generics.ListCreateAPIView):
  queryset = Hospital.objects.all()
  serializer_class = HospitalSerializer


class HospitalDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Hospital.objects.all()
  serializer_class = HospitalSerializer



class HospitalSearchByName(generics.ListAPIView):
    serializer_class = HospitalSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Hospital.objects.filter(name=name)


class HospitalSearchByCategory(generics.ListAPIView):
    serializer_class = HospitalSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Hospital.objects.filter(category=category)


class HospitalSearchByAddress(generics.ListAPIView):
    serializer_class = HospitalSerializer

    def get_queryset(self):
        address = self.kwargs['address']
        return Hospital.objects.filter(address=address)


