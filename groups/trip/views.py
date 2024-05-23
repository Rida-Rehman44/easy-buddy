from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Trip, Event
from .forms import TripForm
from weatherapi.views import get_weather_data


def index(request):
    return render(request, 'base.html')

@login_required
def home(request):
    user_memberships = Trip.objects.all()
    return render(request, 'home.html', {'user_memberships': user_memberships})

@login_required
def create_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.owner = request.user
            trip.save()
            form.save_m2m()  # Save many-to-many relationships if any
            messages.success(request, 'Trip created successfully.')
            return redirect('trip:trip_detail', trip_id=trip.id)
    else:
        form = TripForm()
    return render(request, 'create_trip.html', {'form': form})

@login_required
def search_trip(request):
    trips = Trip.objects.all()
    return render(request, 'search_trip.html', {'trips': trips})

@csrf_exempt
@login_required
def join_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    if request.method == 'POST':
        trip.members.add(request.user)
        messages.success(request, 'You have joined the trip successfully.')
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

@login_required
def trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    events = Event.objects.filter(trip=trip)
    weather_data = None

    if trip.latitude and trip.longitude:
        weather_data = get_weather_data(trip.latitude, trip.longitude)

    # Pass trip, weather, and events data to the template
    return render(request, 'trip_detail.html', {
        'trip': trip,
        'weather_data': weather_data,
        'events': events
    })
################Calender

