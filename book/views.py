from django.shortcuts import render
from django.utils import timezone
import book.models as models

# Create your views here.


def get_rooms_list(request):
    rooms = models.Room.objects.all()
    for room in rooms:
        # "Free" if room.booking.end_time > timezone.now() > room.booking.start_time else "Busy"
        print(room)
        try:
            booking = models.Booking.objects.get(room=room.number)
            room.priore = "Free" if booking.end_time > timezone.now() > booking.start_time else "Busy"
        except:
            room.priore = "Free"
    context = {
        'rooms': rooms
    }
    return render(request, 'book/rooms_list.html', context)