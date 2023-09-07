from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView

from Hotel_Admin.models import *


# Create your views here.

def show_index_page(request):
    context = {"RoomAmount": Rooms.objects.count(), "ClientAmount": Client.objects.count(),
               "ApplicationAmount": RoomApplication.objects.count()}
    return render(request, 'admin_index.html', context=context)


class ShowRoomsPage(ListView):
    model = Rooms
    template_name = 'admin_rooms.html'
    context_object_name = 'rooms'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ApplicationAmount'] = RoomApplication.objects.count()
        return context


class CreateRoomPage(CreateView):
    model = Rooms
    template_name = 'add_room.html'
    fields = '__all__'
    redirect_field_name = 'admin_rooms'
    success_url = reverse_lazy('rooms_admin')


class DeleteRoomPage(DeleteView):
    model = Rooms
    template_name = 'delete_room.html'
    slug_field = "slug"
    slug_url_kwarg = "slug_param"
    success_url = reverse_lazy("rooms_admin")
    context_object_name = "Room"


def show_change_hidden_page(request, slug_param):
    if request.method == 'POST':
        room = Rooms.objects.get(slug=slug_param)
        room.is_hidden = not room.is_hidden
        room.save()
        return redirect('rooms_admin')

    return render(request, 'change_hidden.html')


class ShowApplicationPage(ListView):
    model = RoomApplication
    template_name = 'admin_applications.html'
    context_object_name = 'applications'


class ShowRoomDetailApplicationPage(DetailView):
    model = Rooms
    template_name = 'application_detail.html'
    context_object_name = 'application'
    slug_field = 'id'
    slug_url_kwarg = "id_param"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Client'] = Client.objects.get(id=self.kwargs['id_param'])
        context['Room'] = Rooms.objects.get(id=self.kwargs['id_param'])
        return context


def change_status_true(request, id_param):
    if request.method == 'POST':
        application = RoomApplication.objects.get(id=id_param)
        application.approve_status = True
        application.save()
        return redirect('admin_applications')

    return render(request, 'change_hidden.html')


def change_status_false(request, id_param):
    if request.method == 'POST':
        application = RoomApplication.objects.get(id=id_param)
        application.approve_status = False
        application.save()
        return redirect('admin_applications')

    return render(request, 'change_hidden.html')
