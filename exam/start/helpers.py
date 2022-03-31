from .models import Schedule, Rooms


def suitable_room(filt, room):
    if filt.activity == 'rest' and room.activity != 'rest':
        return False
    if filt.activity == 'meeting' and room.activity != 'meeting':
        return False
    if filt.activity == 'work' and room.activity == 'rest':
        return False

    if filt.capacity > room.capacity:
        return False
    schedule = list(i for i in Schedule.objects.all()
                    if str(i.room_id) == str(room))
    for plan in schedule:
        bad1 = plan.start <= filt.date_start <= plan.finish
        bad2 = plan.start <= filt.date_finish <= plan.finish
        if bad1 or bad2:
            return False
    return True


def suitable_select(selection, filtration):
    if not filtration:
        return False

    rooms_id = list(room.id for room in Rooms.objects.all() if suitable_room(filtration, room))

    return selection.numb in rooms_id


def filtered_rooms(filtration):
    return list(room for room in Rooms.objects.all() if suitable_room(filtration, room))


def add_schedule(filtration, id_):
    new_sch = 0
    rooms_ = Rooms.objects.all()
    for i in range(len(rooms_)):
        if rooms_[i].id == id_:
            new_sch = Schedule(room_id=rooms_[i], start=filtration.date_start, finish=filtration.date_finish)
    new_sch.save()