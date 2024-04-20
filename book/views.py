from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse
from booking_sys.language import get_list_language, set_language

import datetime
from calendar import monthrange
from django.utils import timezone

import book.models as models

# Create your views here.

def get_index(request):
    context = {'language': get_list_language(request.session.get('language'))}
    return redirect('rooms')#render(request, 'book/index.html', context)

def get_rooms_list(request):
    rooms = models.Room.objects.filter(**{key: int(value) for key, value in request.GET.items() 
                                          if value!='' and 
                                          key in ['price__gt', 'price__lt', 'capacity']}).filter(
                                       **{'tags__name':value for key, value in request.GET.items()
                                          if key == 'category' and value != 'all'})
    
    tags = [tag for tag in request.GET.keys() if tag in ['Bathroom_included', 'Refrigerator_included', 'Image']]
    if tags != []:
        for tag in tags:
            rooms = rooms.filter(tags__name=tag)

    for key, value in request.GET.items():
        if key == 'sort_by':
            if value == 'number':
                sort_by = value
            elif value == 'price_decreasing':
                sort_by = '-price'
            elif value == 'price_increase':
                sort_by = 'price'
            else:
                sort_by = f'-{value}'
            rooms = rooms.order_by(sort_by)

    last_form = dict(request.GET.items())
    for room in rooms:
        try:
            booking = models.Booking.objects.get(room=room)
            room.priore = "busy" if booking.end_time > timezone.now() > booking.start_time else "free"
        except:
            room.priore = "free"
    context = {
        'rooms': rooms,
        'language': get_list_language(request.session.get('language')),
        'last_form': last_form
    }
    return render(request, 'book/rooms_list.html', context)


def get_rooms_details(request, pk: int):
    try:
        room = models.Room.objects.get(number=pk)
        today = timezone.now()
        first_day_of_month = datetime.date(today.year, today.month, 1)
        last_day_of_month = datetime.date(today.year, today.month, monthrange(today.year, today.month)[1])
        bookings = models.Booking.objects.filter(room=room, start_time__range=(first_day_of_month, last_day_of_month))

        booked_days = []
        for book in bookings:
            for day in range(book.start_time.day, book.end_time.day+1):
                booked_days.append(day)

        days_of_month = range(1, monthrange(today.year, today.month)[1] + 1)
        context = {
            'room': room,
            'booked_days': booked_days,
            'days_of_month': days_of_month,
            'today': today,
            'language': get_list_language(request.session.get('language'))
        }

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
def booking_form(request, pk):
    if request.method == 'GET':
        return render(request, 'book/booking_form.html', {'language': get_list_language(request.session.get('language'))})
    
    elif request.method == 'POST':
        room_number = pk
        start_number = request.POST.get('start_time')
        end_number = request.POST.get('end_time')
        try:
            room = models.Room.objects.get(number=room_number)
        except ValueError:
            return HttpResponse('wrong room_number', status=400)
        except models.Room.DowsNotExist:
            return HttpResponse('Room does not exist', status=404)
        
        booking = models.Booking.objects.create(room=room,
            user=request.user,
            start_time=start_number,
            end_time=end_number
            )
    
        return redirect('room_detail', pk=pk)

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

