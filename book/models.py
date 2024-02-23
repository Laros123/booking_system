from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    number=models.IntegerField()
    capacity=models.IntegerField()
    location=models.TextField()
    def __str__(self) -> str:
        return f'''number: {self.number}
          capacity: {self.capacity}
          location: {self.location}  
        '''
    class Meta:
        ordering=['number']
        verbose_name='Room'
        verbose_name_plural='Rooms'
    

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING, related_name='booking')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='booking')
    start_time = models.DateTimeField(default=None)
    end_time = models.DateTimeField(default=None)
    creation_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'''number: {self.room}'''
