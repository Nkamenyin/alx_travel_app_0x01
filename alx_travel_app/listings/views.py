from django.shortcuts import render
from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

# Create your views here.
class ListingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing listings.
    Provides list, retrieve, create, update, and delete operations.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing bookings.
    Provides list, retrieve, create, update, and delete operations.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer