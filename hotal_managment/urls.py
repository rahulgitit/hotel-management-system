from django.urls import path,include
from rest_framework.routers import DefaultRouter
from hotal_managment import views
router=DefaultRouter()
router.register('roomapi', views.RoomListCreate, basename="roomapi")
router.register('bookapi', views.RoomListCreate, basename="bookapi")
router.register('customerapi', views.RoomListCreate, basename="customerapi")

# from .views import RoomListCreate, CustomerListCreate, BookingListCreate, BookingDetail, check_availability

urlpatterns = [
    # path('rooms/', RoomListCreate.as_view(), name='room-list-create'),
    # path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    # path('bookings/', BookingListCreate.as_view(), name='booking-list-create'),
    # path('bookings/<int:pk>/', BookingDetail.as_view(), name='booking-detail'),
    # path('availability/', check_availability, name='check-availability'),

    path("", include(router.urls))
]