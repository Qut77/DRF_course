from rest_framework import generics, viewsets
from .models import Trip, Destination
from .serializers import TripSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    @action(methods=['get'], detail=False)
    def destination(self, request):
        destinations = Destination.objects.all()
        return Response({'destination': [d.title for d in destinations]})