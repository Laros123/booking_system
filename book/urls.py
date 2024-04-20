from django.contrib import admin
import book.views as views
from django.urls import path


urlpatterns = [
    path('rooms/', views.get_rooms_list, name='rooms'),
    path('room/<int:pk>', views.get_rooms_details, name='room_detail'),
    path('room/', views.rooms_details_form, name='room_detail_form'),
    path('booking/<int:pk>', views.booking_form, name='booking_form'),
    #path('booking/<int:pk>', views.booking_detail, name='booking_detail'),
    path('', views.get_index, name='index'),
]
