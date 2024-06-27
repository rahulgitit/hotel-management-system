from django.contrib import admin
from hotal_managment.models import Room, Customer,Booking
# Register your models here.

@admin.register(Room)
class roomAdmin(admin.ModelAdmin):
    list_display=["id","number","room_type","price","is_available"]

    

@admin.register(Customer)
class customerAdmin(admin.ModelAdmin):
    list_display=["id","first_name","last_name","email","phone"]

    


@admin.register(Booking)
class bookingAdmin(admin.ModelAdmin):
    list_display=["id","room","customer","check_in","check_out"]
