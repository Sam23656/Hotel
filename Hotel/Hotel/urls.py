"""
URL configuration for Hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Hotel_Client.views import show_index_page, ShowRoomsPage, ShowRoomDetailPage, show_reservation_page, ShowAplicationsPage, delete_application

urlpatterns = [
    path('', show_index_page, name='index'),
    path('rooms/', ShowRoomsPage.as_view(), name='rooms'),
    path('room_detail/<slug:slug>/', ShowRoomDetailPage.as_view(), name='room_detail'),
    path('reservation/<slug:slug>/', show_reservation_page, name='reservation'),
    path('applications/', ShowAplicationsPage.as_view(),name='applications'),
    path('delete_application/<int:pk>/', delete_application, name='delete_application'),
    path('admin/', admin.site.urls),
]
