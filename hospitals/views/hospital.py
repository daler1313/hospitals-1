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
