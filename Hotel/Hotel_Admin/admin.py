from django.contrib import admin

# Register your models here.
from Hotel_Admin.models import Service, Rooms, RoomApplication

admin.site.register(Service)
admin.site.register(Rooms)
admin.site.register(RoomApplication)
