from django.urls import path
from .views import SafariPackageList, SafariPackageDetail,DestinationList,DestinationDetail,SafariBookingCreate,SafariAdventureList,home

urlpatterns = [
    path('',home),
    path('safari-packages/', SafariPackageList.as_view(), name='safari-list'),
    path('safari-packages/<slug:slug>/', SafariPackageDetail.as_view(), name='safari-detail'),
     path('destinations/', DestinationList.as_view(), name='destination-list'),
    path('destinations/<slug:slug>/', DestinationDetail.as_view(), name='destination-detail'),
    path('bookings/', SafariBookingCreate.as_view(), name='safari-booking'),
    path('safari-adventures/', SafariAdventureList.as_view(), name='safari-adventure-list'),
    
    
]