from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, Message


@login_required
def chat_room_view(request, room_id):
    # Retrieve the chat room based on the provided room_id
    room = get_object_or_404(ChatRoom, id=room_id)
    # Retrieve the latest 50 messages from the chat room
    messages = Message.objects.filter(chat_room=room).order_by("-timestamp")[:50]
    # Render the chat room template and pass the room and messages as context
    return render(request, "chat/chat_room.html", {"room": room, "messages": messages})


@login_required
def send_message(request, room_id):
    # Check if the request method is POST
    if request.method == "POST":
        # Retrieve the chat room based on the provided room_id
        room = get_object_or_404(ChatRoom, id=room_id)
        # Get the message content from the request POST data
        message_content = request.POST.get("message", "")

        # Ensure message content is not empty
        if not message_content:
            return JsonResponse(
                {"status": "error", "message": "Message content is required."},
                status=400,
            )

        # Create a new message in the chat room
        new_message = Message(
            chat_room=room, sender=request.user, content=message_content
        )
        new_message.save()

        # Return a JSON response indicating success and include the new message ID
        return JsonResponse({"status": "ok", "message_id": new_message.id})

    # Return a JSON response indicating an error for invalid request methods
    return JsonResponse(
        {"status": "error", "message": "Invalid request method."}, status=400
    )
