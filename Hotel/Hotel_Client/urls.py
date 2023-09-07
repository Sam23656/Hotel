from django.urls import path

from Hotel_Client.views import *

urlpatterns = [
    path('', show_index_page, name='index'),
    path('rooms/', ShowRoomsPage.as_view(), name='rooms'),
    path('room_detail/<slug:slug>/', ShowRoomDetailPage.as_view(), name='room_detail'),
    path('reservation/<slug:slug>/', show_reservation_page, name='reservation'),
    path('applications/', ShowAplicationsPage.as_view(), name='applications'),
    path('delete_application/<int:pk>/', delete_application, name='delete_application'),
]