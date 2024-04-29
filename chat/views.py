from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import ChatRoom, Message

def chat_room_view(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    return render(request, 'chat/chat_room.html', {'room': room})

def send_message(request, room_id):
    if request.method == 'POST':
        room = get_object_or_404(ChatRoom, id=room_id)
        message = request.POST['message']
        new_message = Message(chat_room=room, sender=request.user, content=message)
        new_message.save()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)
