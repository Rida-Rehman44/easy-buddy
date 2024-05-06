from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Group, GroupMembership
from django.shortcuts import redirect
from django.contrib import messages

@login_required
def home_view(request):
    # Retrieve the groups the user has joined
    user_groups = GroupMembership.objects.filter(user=request.user)
    
    # Render the 'home.html' template with the user groups
    return render(request, 'groups/home.html', {'user_groups': user_groups})


@login_required
def create_group(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        description = request.POST.get('description')
        if name and location and description:
            group = Group.objects.create(
                name=name,
                location=location,
                description=description,
                owner=request.user
            )
            GroupMembership.objects.create(user=request.user, group=group, role='owner')
            messages.success(request, 'Group created successfully.')
            return redirect('group_detail', group_id=group.id)
    return render(request, 'groups/create_group.html')

@login_required
def search_group(request):
    groups = Group.objects.filter(is_open=True)  # Assuming 'is_open' indicates whether a group is open for new members
    return render(request, 'groups/search_group.html', {'groups': groups})


@login_required
def join_group(request, group_id):
    group = Group.objects.get(id=group_id)
    if request.method == 'POST':
        GroupMembership.objects.create(user=request.user, group=group, role='member')
        messages.success(request, 'You have joined the group successfully.')
        return redirect('group_detail', group_id=group_id)
    return render(request, 'groups/join_group.html', {'group': group})
