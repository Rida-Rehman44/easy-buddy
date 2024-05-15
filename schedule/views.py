

from django.shortcuts import render,redirect
from django.urls import reverse
from . import models




# Create your views here.


def list(request):
    all_artist = models.Artist.objects.all()
    context = {'all_artist':all_artist}
    
    if request.POST:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        models.Artist.objects.create(firstname=firstname, lastname=lastname)
        # if user submitted new artist --- > list.html
        return redirect(reverse('schedule:list'))
    else:
        return render(request, 'schedule/list.html',context=context)


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
    if request.POST:
        pk = request.POST['pk']
        try:
            models.Artist.objects.get(pk=pk).delete
            return redirect(reverse('schedule:delete'))
        except:
            print('pk not found!')
            return redirect(reverse('schedule:delete'))
    
    else:
    
        return render(request, 'schedule/delete.html')





