from datetime import datetime

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

# Create your views here.
from Hotel_Admin.models import Rooms, RoomApplication, Service
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ApplicationAmount'] = RoomApplication.objects.count()
        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ApplicationAmount'] = RoomApplication.objects.count()
        return context


def show_reservation_page(request, slug):
    context = {"form": ReservationForm(), "room": Rooms.objects.get(slug=slug),
               "ApplicationAmount": RoomApplication.objects.count()}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        middle_name = request.POST['middle_name']
        email = request.POST['email']
        person_count = request.POST['person_count']

        start_time_month = int(request.POST['start_time_month'])
        start_time_day = int(request.POST['start_time_day'])
        start_time_year = int(request.POST['start_time_year'])
        start_time = datetime(start_time_year, start_time_month, start_time_day)

        end_time_month = int(request.POST['end_time_month'])
        end_time_day = int(request.POST['end_time_day'])
        end_time_year = int(request.POST['end_time_year'])
        end_time = datetime(end_time_year, end_time_month, end_time_day)

        services = request.POST.getlist('services')

        room = Rooms.objects.get(slug=slug)

        service_price = 0
        for service in services:
            serc = Service.objects.get(pk=service)
            service_price += serc.price

        total_price = room.price + (int(person_count) * room.price) + service_price
        client = Client()
        client.first_name = first_name
        client.last_name = last_name
        client.middle_name = middle_name
        client.email = email
        client.save()

        latest_client = Client.objects.latest('pk')

        room_apl = RoomApplication()
        room_apl.client_id = latest_client
        room_apl.room_id = room
        room_apl.start_time = start_time
        room_apl.end_time = end_time
        room_apl.total_price = total_price
        room_apl.save()

        room_apl = RoomApplication.objects.latest('pk')
        for service_id in services:
            serc = Service.objects.get(pk=service_id)
            room_apl.services.add(serc)

        room_apl.save()

        room.reserved = True
        room.save()
        return redirect('rooms')

    return render(request, 'reservation.html', context=context)


class ShowAplicationsPage(ListView):
    model = RoomApplication
    template_name = 'applications.html'
    context_object_name = 'applications'


def delete_application(request, pk):
    application = RoomApplication.objects.get(pk=pk)
    application.delete()
    return redirect('rooms')

