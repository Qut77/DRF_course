from rest_framework import generics
from rest_framework.response import Response
from .models import Trip
from .serializers import TripSerializer

class TripAPIList(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripAPIUpdate(generics.UpdateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripAPIcrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
