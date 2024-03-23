from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse
from booking_sys.language import get_list_language

import book.models as models

# Create your views here.

def get_index(request):
    context = {'language': get_list_language(request.session.get('language'))}
    return render(request, 'book/index.html', context)

def get_rooms_list(request):
    rooms = models.Room.objects.filter(**{key: int(value) for key, value in request.GET.items() if value!=''})
    for room in rooms:
        try:
            booking = models.Booking.objects.get(room=room)
            room.priore = "busy" if booking.end_time > timezone.now() > booking.start_time else "free"
        except:
            room.priore = "free"
    context = {
        'rooms': rooms,
        'language': get_list_language(request.session.get('language'))
    }
    return render(request, 'book/rooms_list.html', context)


def get_rooms_details(request, pk: int):
    try:
        room = models.Room.objects.get(number=pk)
    except:
        room = {}
    context = {
        'room': room,
        'language': get_list_language(request.session.get('language'))
    }
    return render(request, 'book/room_detail.html', context)

def rooms_details_form(request):
    if request.method == 'POST':
        room_number = request.POST.get('room_number')
        return redirect('room_detail', pk=int(room_number))

@login_required
def booking_form(request):
    if request.method == 'GET':
        return render(request, 'book/booking_form.html', {'language': get_list_language(request.session.get('language'))})
    
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
            'booking': booking, 
            'language': get_list_language(request.session.get('language'))
        }
        return render(request, 'book/booking_detail.html', context)
    
    elif request.method == 'POST':
        ...