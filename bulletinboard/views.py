from django.shortcuts import render, redirect
from .models import BulletinBoardMessage
from .forms import BulletinBoardMessageForm

def create_bulletin_board_message(request):
    if request.method == 'POST':
        form = BulletinBoardMessageForm(request.POST, request.FILES)
        if form.is_valid():
            bulletin_board_message = form.save(commit=False)
            bulletin_board_message.author = request.user
            bulletin_board_message.group = request.user.group_set.first()  # Assuming user is associated with only one group
            bulletin_board_message.save()
            return redirect('group_detail', group_id=bulletin_board_message.group.id)
    else:
        form = BulletinBoardMessageForm()
    return render(request, 'create_bulletin_board_message.html', {'form': form})

def bulletin_board_view(request):
    bulletin_board_messages = BulletinBoardMessage.objects.all()
    return render(request, 'bulletin_board.html', {'bulletin_board_messages': bulletin_board_messages})
