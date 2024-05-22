from django.urls import path
from .views import home, create_trip, search_trip, join_trip, trip_detail

app_name = 'trip'

urlpatterns = [
    path('create/', create_trip, name='create_trip'),
    path('search/', search_trip, name='search_trip'),
    path('join/<int:trip_id>/', join_trip, name='join_trip'),
    path('trip_detail/<int:trip_id>/', trip_detail, name='trip_detail'),
    path('home/', home, name='home'),
    # Use views from bulletin_board app


]
