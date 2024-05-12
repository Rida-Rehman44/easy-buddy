import uuid

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from .models import Event
from .forms import EventForm


@login_required
def event_list(request):
    events = Event.objects.filter(group__in=request.user.groups.all())
    return render(request, 'events/event_list.html', {'events': events})


@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            group = Group.objects.create(name=event.name+str(uuid.uuid4()))
            user_emails = request.POST.get('users')
            emails = user_emails.replace(' ', '').split(',')
            users = User.objects.filter(email__in=emails)
            group.user_set.set(users)
            group.user_set.add(request.user)  # Add creating user to the group
            event.admin_user = request.user  # Set creating user as the group admin
            group.save()  # Save the group to generate an ID
            event.group = group
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})


@login_required
def event_edit(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    emails=[]
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            user_emails = request.POST.get('users')
            emails = user_emails.replace(' ', '').split(',')
            users = User.objects.filter(email__in=emails)
            event.group.user_set.set(users)
            event.group.user_set.add(request.user)
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
        users = event.group.user_set.all()
        emails = ', '.join(map(lambda u: u.email, users))

    return render(request, 'events/event_form.html', {'form': form, 'event': event, 'users': emails})