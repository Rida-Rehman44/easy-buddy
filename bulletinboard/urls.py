# urls.py
from django.urls import path
from .views import create_bulletin_board_message

urlpatterns = [
    # Other URL patterns...
    path('create_bulletin_board_message/', create_bulletin_board_message, name='create_bulletin_board_message'),
]
