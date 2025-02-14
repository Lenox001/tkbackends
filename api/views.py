from rest_framework import generics
from .models import SafariPackage,Destination,SafariBooking,SafariAdventure
from .serializers import SafariPackageSerializer,DestinationSerializer,SafariBookingSerializer,SafariAdventureSerializer
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to TK Safaris  API!"})

class SafariPackageList(generics.ListCreateAPIView):
    queryset = SafariPackage.objects.all().prefetch_related('itinerary')  # Preload itinerary data
    serializer_class = SafariPackageSerializer

class SafariPackageDetail(generics.RetrieveAPIView):
    queryset = SafariPackage.objects.all().prefetch_related('itinerary')  # Preload itinerary data
    serializer_class = SafariPackageSerializer
    lookup_field = 'slug'

class DestinationList(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    def get_queryset(self):
        return Destination.objects.only("image", "title", "slug")


class DestinationDetail(generics.RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    lookup_field = 'slug'

class SafariBookingCreate(generics.CreateAPIView):
    queryset = SafariBooking.objects.all()
    serializer_class = SafariBookingSerializer
    
class SafariAdventureList(generics.ListCreateAPIView):
    queryset = SafariAdventure.objects.all()
    serializer_class = SafariAdventureSerializer