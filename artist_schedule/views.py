from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

def list_schedule(request):
    all_artist = models.Artist.objects.all()
    context = {'all_artist': all_artist}
    
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        models.Artist.objects.create(firstname=firstname, lastname=lastname)
        return redirect(reverse('artist_schedule:list_schedule'))
    else:
        return render(request, 'list_schedule.html', context=context)

def add_schedule(request):
    if request.method == 'POST':
        day = request.POST['day']
        stage = request.POST['stage']
        hours = request.POST['hours']
        genre = request.POST['genre']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        models.Artist.objects.create(day=day, stage=stage, hours=hours, genre=genre, firstname=firstname, lastname=lastname)
        return redirect(reverse('artist_schedule:add_schedule'))
    else:
        return render(request, 'add_schedule.html')

def delete_schedule(request):
    if request.method == 'POST':
        pk = request.POST['pk']
        try:
            artist = models.Artist.objects.get(pk=pk)
            artist.delete()
            return redirect(reverse('artist_schedule:delete_schedule'))
        except models.Artist.DoesNotExist:
            print('pk not found!')
            return redirect(reverse('artist_schedule:delete_schedule'))
    else:
        return render(request, 'delete_schedule.html')
