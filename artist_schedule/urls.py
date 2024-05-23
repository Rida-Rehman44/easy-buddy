from django.urls import path
from . import views

app_name = 'artist_schedule'

urlpatterns = [
    path('list_schedule/', views.list_schedule, name='list_schedule'),
    path('add_schedule/', views.add_schedule, name='add_schedule'),
    path('delete_schedule/', views.delete_schedule, name='delete_schedule'),
]
