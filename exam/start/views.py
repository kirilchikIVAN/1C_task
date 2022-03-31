from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Rooms, Schedule, Filter, SelectedRoom
from .forms import FilterFrom, SelectedRoomForm
from .helpers import suitable_room, suitable_select, filtered_rooms, add_schedule
from django.shortcuts import redirect


# Create your views here.
def home(request):
    if request.method == 'POST':
        return redirect(filtering)
    return render(request, 'start/home.html')


def filtering(request, filtration=None):
    error, your_filter = '', ''
    if request.method == 'POST':
        filt = FilterFrom(request.POST)

        if filt.is_valid():
            filt.save()
            filtration = Filter.objects.all().last()
            if filtered_rooms(filtration):
                return redirect(rooms)
            else:
                error = 'Все комнаты заняты, выберите другое время'
                your_filter = 'Ваш фильтр:'
        else:
            error = 'Неправильно заполнена форма'

    filt_form = FilterFrom()

    rooms_ = Rooms.objects.all()

    if filtration:
        temp = list(i for i in rooms_ if suitable_room(filtration, i))
        rooms_ = list(temp)

    context = {
        'title': 'rooms',
        'rooms': rooms_,
        'form': filt_form,
        'filter': filtration,
        'error': error,
        'your_filter': your_filter,
    }
    return render(request, 'start/filtering.html', context)


def rooms(request):
    filtration = Filter.objects.all().last()
    if not filtration:
        return redirect(filtering)

    error = ''
    if request.method == 'POST':
        select = SelectedRoomForm(request.POST)
        if select.is_valid():
            select.save()
            selection = SelectedRoom.objects.all().last()
            filtration = Filter.objects.all().last()
            if suitable_select(selection, filtration):
                add_schedule(filtration, selection.numb)
                return redirect(home)
            else:
                error = 'Некорректно введен номер'
        else:
            error = 'Некорректный ввод'

    rooms_ = filtered_rooms(filtration)

    select_form = SelectedRoomForm()

    context = {
        'title': 'rooms',
        'rooms': rooms_,
        'filter': filtration,
        'select': select_form,
        'error': error
    }
    return render(request, 'start/rooms.html', context)


def about(request):
    context = {
        "author": "Иванчик К.А.",
        "date": datetime.now(),
    }
    return render(request, 'start/about.html', context)
