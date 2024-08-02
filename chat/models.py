from django.db import models
from datetime import datetime
from account.models import User

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
class Message(models.Model):
    value = models.CharField(max_length=3000)
    date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    def __str__(self):
        return self.value