from django.contrib.auth.models import User
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=30)
    size = models.IntegerField(null=True, default=0)
    color = models.CharField(max_length=7, default='#007bff')    

    def __str__(self):
        return self.name

class Live(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_room')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_live')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room