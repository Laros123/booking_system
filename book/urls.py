from django.contrib import admin
import book.views as views
from django.urls import path


urlpatterns = [
    path('rooms/', views.get_rooms_list),
]
