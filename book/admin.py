from django.contrib import admin
from book.models import Room, Booking, Tag
# Register your models here.

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Tag)

