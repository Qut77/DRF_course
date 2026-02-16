from rest_framework import serializers
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('title', 'description', 'created_at', 'updated_at', 'is_visible', 'destination')