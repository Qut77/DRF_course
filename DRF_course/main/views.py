from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Trip
from .serializers import TripSerializer

# class TripAPIView(generics.ListAPIView):
#     queryset = Trip.objects.all()
    # serializer_class = TripSerializer

class TripAPIView(APIView):
    def get(self, request):
        t = Trip.objects.all()
        return Response({'posts': TripSerializer(t, many=True).data})
    
    def post(self, request):
        serializer = TripSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
