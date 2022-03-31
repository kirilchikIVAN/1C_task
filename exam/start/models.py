from django.db import models

# Create your models here.


class Rooms(models.Model):
    id = models.IntegerField(primary_key=True)
    capacity = models.IntegerField()
    activity = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id) + ' '\
               + str(self.capacity) + ' '\
               + str(self.activity)


class Schedule(models.Model):
    room_id = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    start = models.DateTimeField()
    finish = models.DateTimeField()

    def id(self):
        return str(self.room_id)

    def __str__(self):
        return str(self.room_id) + ' '\
               + str(self.start) + ' '\
               + str(self.finish)


class Filter(models.Model):
    capacity = models.IntegerField()
    activity = models.CharField(max_length=20)
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()


class SelectedRoom(models.Model):
    numb = models.IntegerField()


