from rest_framework import generics, status
from rest_framework.response import Response
from .models import Room, Customer, Booking
from .serializers import RoomSerializer, CustomerSerializer, BookingSerializer
from django.http import JsonResponse
from datetime import date
from rest_framework.viewsets import ModelViewSet

class RoomListCreate(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class CustomerListCreate(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class BookingListCreate(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        room = Room.objects.get(id=data['room'])
        bookings = Booking.objects.filter(room=room, check_out__gte=data['check_in'], check_in__lte=data['check_out'])
        if bookings.exists():
            return Response({"error": "Room is not available for the selected dates"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def check_availability(request):
    check_in = request.GET.get('check_in')
    check_out = request.GET.get('check_out')
    available_rooms = Room.objects.filter(is_available=True, booking__check_out__lt=date.fromisoformat(check_in)).union(Room.objects.filter(is_available=True,booking__check_in__gt=date.fromisoformat(check_out))
    )
    serializer = RoomSerializer(available_rooms, many=True)
    return JsonResponse(serializer.data, safe=False)
