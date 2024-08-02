from django.shortcuts import render,redirect,get_object_or_404
from .models import Room , Message
from django.http import HttpResponse,JsonResponse,HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from account.models import User
# Create your views here.
@login_required
def home(request):
	return render(request,'chat/home.html')
@login_required
def room(request,room):
    username = request.user.username
    room_detail = Room.objects.get(name=room)
    return render(request,'chat/room.html',{'room':room,"username":username,"room_detail":room_detail})
@login_required
def checkview(request):
    room = request.POST['room_name']
    if Room.objects.filter(name=room).exists():
        return redirect('/chat/'+room)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/chat/'+room)
@login_required
def send(request):
    message = request.POST['message']
    user = request.user
    room_id = request.POST['room_id']
    room = get_object_or_404(Room, id=room_id)
    new_message = Message.objects.create(value=message, user=user, room=room)
    new_message.save()
    return HttpResponse('Message sent successfully')
@login_required
def getMessages(request,room):
     room_details = Room.objects.get(name=room)
     message =Message.objects.filter(room=room_details.id)
     message_list = []
     for message in message:
          message_list.append({
               "value": message.value,
               "date": message.date,
               "user": message.user.username,
               "room": message.room.id,
               "id": message.id,
               "room_name": message.room.name,
               'picture_user':message.user.picture.url,
               })
     return JsonResponse({"messages": message_list})

@login_required
def delete_message(request):
    if request.method == 'POST':
        msg_id = request.POST.get('message')
        room_id = request.POST.get('room_id')
        room_name = request.POST.get('room_name')
        user = request.user
        message = Message.objects.get(id=msg_id,room=room_id)
        # message = get_object_or_404(Message, id=msg_id, user=user,room=room_id)
        if user != message.user:
            return redirect('/chat/'+room_name)
        else:
            message.delete()
            return redirect('/chat/'+room_name)