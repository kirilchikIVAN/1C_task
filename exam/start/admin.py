from django.contrib import admin
from .models import Rooms, Schedule, Filter, SelectedRoom

# Register your models here.


admin.site.register(Rooms)
admin.site.register(Schedule)
admin.site.register(Filter)
admin.site.register(SelectedRoom)
