from django.urls import path

from Hotel_Admin.views import *

urlpatterns = [
    path('', show_index_page, name='index_admin'),
    path('rooms/', ShowRoomsPage.as_view(), name='rooms_admin'),
    path('delete_room/<slug:slug_param>/', DeleteRoomPage.as_view(), name='delete_room'),
    path('change_hidden/<slug:slug_param>/', show_change_hidden_page, name='change_hidden'),
    path('admin_aplications/', ShowApplicationPage.as_view(), name='admin_applications'),
    path('admin_aplications/<int:id_param>/', ShowRoomDetailApplicationPage.as_view(), name='application_detail'),
    path('change_status_false/<int:id_param>/', change_status_false, name='change_status_false'),
    path('change_status_true/<int:id_param>/', change_status_true, name='change_status_true'),
    path('add_room/', CreateRoomPage.as_view(), name='add_room'),
]
