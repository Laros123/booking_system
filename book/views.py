from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse

import book.models as models

# Create your views here.

def get_index(request):
    context = {}
    return render(request, 'book/index.html', context)


def get_rooms_list(request):
    rooms = models.Room.objects.all()
    for room in rooms:
        try:
            booking = models.Booking.objects.get(room=room.number)
            room.priore = "Free" if booking.end_time > timezone.now() > booking.start_time else "Busy"
        except:
            room.priore = "Free"
    context = {
        'rooms': rooms
    }
    return render(request, 'book/rooms_list.html', context)


def get_rooms_details(request, room_id: int):
    room = models.Room.objects.get(id=room_id)
    context = {
        'room': room
    }
    return render(request, 'book/room_detail.html', context)

def rooms_details_form(request):
    if request.method == 'POST':
        room_number = request.POST.get('room_number')
        return redirect('room_detail', room_id=int(room_number))


def booking_form(request):
    if request.method == 'GET':
        return render(request, 'book/booking_form.html')
    
    elif request.method == 'POST':
        room_number = request.POST.get('room_number')
        start_number = request.POST.get('start_time')
        end_number = request.POST.get('end_time')
        try:
            room = models.Room.objects.get(number=room_number)
            #room = models.Room.objects.create(
            #    room=
            #)
        except ValueError:
            return HttpResponse('wrong room_number', status=400)
        except models.Room.DowsNotExist:
            return HttpResponse('Room does not exist', status=404)
        
        booking = models.Booking.objects.create(room=room,
            user=request.user,
            start_time=start_number,
            end_time=end_number
            )
    
        return redirect('booking_detail', pk=booking.id)

def booking_detail(request, pk: int):
    if request.method == 'GET':
        booking = models.Booking.objects.get(id=pk)
        context = {
            'booking': booking
        }
        return render(request, 'book/booking_detail.html', context)
    
    elif request.method == 'POST':
        ...