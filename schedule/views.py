from django.shortcuts import render

from . import models




# Create your views here.

def list(request):
    all_artist = models.Artist.objects.all()
    context = {'all_artist':all_artist}
    return render(request, 'schedule/list.html',context=context)


def add(request):
    return render(request, 'schedule/add.html')


def delete(request):
    return render(request, 'schedule/delete.html')





