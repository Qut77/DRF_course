from django.shortcuts import render
from rest_framework import generics
from .models import Trip
from .serializers import TripSerializer

class TripAPIView(generics.ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer