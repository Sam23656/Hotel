from django.db import models

# Create your models here.
from Hotel_Client.models import Client


class Service(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.title}"


class Rooms(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    categorys = (("cheap", "дешевый"), ("middle", "средний"), ("expensive", "дорогой"))
    category = models.CharField(choices=categorys, max_length=50, null=True)
    slug = models.SlugField()
    price = models.PositiveIntegerField()
    reserved = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    likes = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title}"


class RoomApplication(models.Model):
    id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    room_id = models.OneToOneField(Rooms, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    start_time = models.DateField()
    end_time = models.DateField()
    total_price = models.PositiveIntegerField(null=True)
    approve = ((False, 'Отклонено'), (True, 'Одобрено'), ("Not checked", 'Не проверено'))
    approve_status = models.CharField(choices=approve, max_length=50, default="Not checked")

    def __str__(self):
        return f"{self.id}"
