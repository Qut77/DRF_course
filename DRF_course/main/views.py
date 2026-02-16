from rest_framework import generics
from rest_framework.response import Response
from .models import Trip
from .serializers import TripSerializer

class TripAPIView(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
