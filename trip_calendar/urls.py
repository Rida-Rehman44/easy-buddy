from django.urls import path
from .views import calendar_home

app_name = 'trip_calendar'

urlpatterns = [

     path('calendar_home/', calendar_home, name='calendar_home'),



    ]