from rest_framework import serializers
from .models import SafariPackage,Destination,SafariBooking,SafariAdventure,SafariItinerary


class SafariItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = SafariItinerary
        fields = ['day_number', 'title', 'description']

class SafariPackageSerializer(serializers.ModelSerializer):
    itinerary = SafariItinerarySerializer(many=True, read_only=True)  # Ensure it's included

    class Meta:
        model = SafariPackage
        fields = ['title', 'overview', 'full_description', 'image', 'slug', 'itinerary']

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['title', 'slug', 'image', 'highlights', 'about', 'features']

        
class SafariBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafariBooking
        fields = '__all__'
        
class SafariAdventureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafariAdventure
        fields = ['id', 'title', 'description', 'image']