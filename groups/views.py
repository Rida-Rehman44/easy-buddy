from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Group, BulletinBoardMessage  # Import Group and BulletinBoardMessage models
from .forms import BulletinBoardMessageForm  # Import BulletinBoardMessageForm
from django.forms import inlineformset_factory, ModelForm, TextInput
from shopping_checklist.models import ShoppingChecklist, ShoppingItem

@login_required
def home_view(request):
    user_groups = request.user.owned_groups.all()  # Retrieve groups owned by the user
    return render(request, 'groups/home.html', {'user_groups': user_groups})

@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.owner = request.user
            group.save()
            form.save_m2m()  # Save many-to-many relationships if any
            messages.success(request, 'Group created successfully.')
            return redirect('group_detail', group_id=group.id)
    else:
        form = GroupForm()
    return render(request, 'groups/create_group.html', {'form': form})

@login_required
def search_group(request):
    groups = Group.objects.filter(is_open=True)
    return render(request, 'groups/search_group.html', {'groups': groups})

@login_required
def join_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        group.members.add(request.user)
        messages.success(request, 'You have joined the group successfully.')
        return redirect('group_detail', group_id=group_id)
    return render(request, 'groups/join_group.html', {'group': group})

@login_required
def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    bulletin_board_messages = BulletinBoardMessage.objects.filter(group=group)
    
    if request.method == 'POST':
        form = BulletinBoardMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group = group
            message.save()
            messages.success(request, 'Bulletin board message posted successfully!')
            return redirect('group_detail', group_id=group_id)
        else:
            messages.error(request, 'Failed to post bulletin board message. Please check the form inputs.')
    else:
        form = BulletinBoardMessageForm()
    
    shopping_lists = ShoppingChecklist.objects.filter(group=group)
    return render(request, 'groups/group_detail.html', {'group': group, 'shopping_lists': shopping_lists, 'bulletin_board_messages': bulletin_board_messages, 'form': form})

@login_required
def create_shopping_checklist(request):
    if request.method == 'POST':
        form = ChecklistForm(request.POST)
        if form.is_valid():
            checklist = form.save(commit=False)
            checklist.user = request.user
            checklist.save()
            messages.success(request, 'Shopping checklist created successfully!')
            return redirect('home_list')
    else:
        form = ChecklistForm()
    return render(request, 'groups/create_shopping_checklist.html', {'form': form})

@login_required
def home_list_view(request):
    # Add any necessary logic here
    return render(request, 'home_list.html')  

class ChecklistForm(ModelForm):
    class Meta:
        model = ShoppingChecklist
        fields = ['name', 'event']  # Include any other fields you want to edit

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'location', 'description']  # Add more fields if necessary

class ShoppingItemForm(ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ['quantity', 'item_name', 'bought']
        widgets = {
            'quantity': TextInput(attrs={'placeholder': 'Quantity', 'class': 'form-control'}),
            'item_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Type to search...',
                                          'list': 'itemList'}),
        }

ShoppingItemFormSet = inlineformset_factory(ShoppingChecklist, ShoppingItem, form=ShoppingItemForm, extra=1)


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