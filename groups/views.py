from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Group, BulletinBoardMessage  # Import Group and BulletinBoardMessage models
from .forms import BulletinBoardMessageForm, ChecklistForm  # Import BulletinBoardMessageForm
from django.forms import inlineformset_factory, ModelForm, TextInput
from shopping_checklist.models import ShoppingChecklist, ShoppingItem
from django.urls import reverse
from .models import Artist
from .forms import ShoppingItemFormSet, ChecklistForm
from .models import ShoppingChecklist
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views import View
from django.shortcuts import redirect
from django.contrib import messages
from .forms import ShoppingItemFormSet, ChecklistForm
from .models import ShoppingChecklist

@login_required
def home(request):
    user_memberships = Group.objects.all()  # Retrieve memberships of the user
    return render(request, 'groups/home.html', {'user_memberships': user_memberships})

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
    # Retrieve the group object based on the provided group_id
    group = get_object_or_404(Group, pk=group_id)
   
    # Retrieve bulletin board messages associated with the group
    #bulletin_board_messages = BulletinBoardMessage.objects.filter(group=group)
    
    # Handle POST request for submitting bulletin board message form
    if request.method == 'POST':
        form = BulletinBoardMessageForm(request.POST)
        if form.is_valid():
            # Save the bulletin board message with the current user and group
            message = form.save(commit=False)
            message.author = request.user
            message.group = group
            message.save()
            messages.success(request, 'Bulletin board message posted successfully!')
            return redirect('group_detail')
        else:
            # Print form errors for debugging
            print(form.errors)
            messages.error(request, 'Failed to post bulletin board message. Please check the form inputs.')
    else:
        # Initialize an empty form for displaying in the template
        form = BulletinBoardMessageForm()
    
    # Retrieve shopping checklists associated with the group
    # shopping_lists = ShoppingChecklist.objects.filter(group=group)
    
    # Debugging: Print request POST data
    print(request.POST)
    
    # Prepare context data to pass to the template
    context = {
        'group': group,
        #'bulletin_board_messages': bulletin_board_messages,
        #'shopping_lists': shopping_lists,
        'form': form,
    }
    
    # Render the template with the context data
    return render(request, 'groups/group_detail.html', context)





@login_required
def create_shopping_checklist(request):
    if request.method == 'POST':
        form = ChecklistForm(request.POST)
        if form.is_valid():
            checklist = form.save(commit=False)
            checklist.user = request.user
            checklist.save()
            messages.success(request, 'Shopping checklist created successfully!')
            return redirect('groups:home_list')
    else:
        form = ChecklistForm()
    return render(request, 'groups/create_shopping_checklist.html', {'form': form})

@login_required
def home_list_view(request):
    # Add any necessary logic here
    return render(request, 'groups/home_list.html', )  




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
    # Your logic here
    return render(request, 'bulletin_board.html')

# New view functions added
def list(request):
    all_artist = models.Artist.objects.all()
    context = {'all_artist': all_artist}
    
    if request.POST:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        models.Artist.objects.create(firstname=firstname, lastname=lastname)
        # if user submitted new artist --- > list.html
        return redirect(reverse('schedule:list'))
    else:
        return render(request, 'schedule/list.html', context=context)


def add(request):
    if request.POST:
        day = request.POST['day']
        stage = request.POST['stage']
        hours = request.POST['hours']
        genre = request.POST['genre']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        models.Artist.objects.create(day=day, stage=stage, hours=hours, genre=genre, firstname=firstname, lastname=lastname)
        # if user submitted new artist --- > list.html
        return redirect(reverse('schedule:add'))
    else:
        return render(request, 'schedule/add.html')


def delete(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        try:
            artist = Artist.objects.get(pk=pk)
            artist.delete()
            messages.success(request, 'Artist deleted successfully.')
        except Artist.DoesNotExist:
            messages.error(request, 'Artist with the given ID does not exist.')
        return redirect(reverse('schedule:delete'))
    else:
        return render(request, 'schedule/delete.html')

class EditView(LoginRequiredMixin, View):
    checklist_form_class = ChecklistForm
    item_formset_class = ShoppingItemFormSet
    template_name = 'group:edit_checklist.html'

    def get(self, request, checklist_id):
        checklist = get_object_or_404(ShoppingChecklist, pk=checklist_id)
        checklist_form = self.checklist_form_class(instance=checklist)
        item_formset = self.item_formset_class(instance=checklist)

        return render(request, self.template_name,
                      {'checklist_form': checklist_form, 'item_formset': item_formset, 'checklist': checklist})

    def post(self, request, checklist_id):
        checklist = get_object_or_404(ShoppingChecklist, pk=checklist_id)
        checklist_form = self.checklist_form_class(request.POST, instance=checklist)
        item_formset = self.item_formset_class(request.POST, instance=checklist)
        if checklist_form.is_valid() and item_formset.is_valid():
            checklist_form.save()
            item_formset.save()
            return redirect('/shopping_checklist/')  # Redirect to home screen after editing
        return render(request, self.template_name,
                      {'checklist_form': checklist_form, 'item_formset': item_formset, 'checklist': checklist})

class DeleteView(LoginRequiredMixin, View):
    def get(self, request, checklist_id):
        checklist = get_object_or_404(ShoppingChecklist, pk=checklist_id)
        return redirect('/shopping_checklist/')  # Redirect to home screen after editing


    def post(self, request, checklist_id):
        checklist = get_object_or_404(ShoppingChecklist, pk=checklist_id)
        checklist.delete()
        return redirect('/shopping_checklist/')  # Redirect to home screen after editing