from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

# Create your views here.
from Hotel_Admin.models import Rooms, RoomApplication
from Hotel_Client.forms import ReservationForm
from Hotel_Client.models import Client


def show_index_page(request):
    context = {"RoomAmount": Rooms.objects.count(), "ClientAmount": Client.objects.count(),
               "ApplicationAmount": RoomApplication.objects.count()}
    return render(request, 'index.html', context=context)


class ShowRoomsPage(ListView):
    model = Rooms
    template_name = 'rooms.html'
    context_object_name = 'rooms'


class ShowRoomDetailPage(DetailView):
    model = Rooms
    template_name = 'room_detail.html'
    context_object_name = 'room'
    slug_field = 'slug'

    def post(self, request, *args, **kwargs):
        room = Rooms.objects.get(slug=self.kwargs['slug'])
        room.likes += 1
        room.save()
        return self.get(request, *args, **kwargs)


def show_reservation_page(request, slug):
    context = {"form": ReservationForm()}
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    return render(request, 'reservation.html', context=context)