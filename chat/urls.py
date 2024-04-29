from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('room/<int:room_id>/', views.chat_room_view, name='chat_room'),
    path('room/<int:room_id>/send/', views.send_message, name='send_message'),
]
