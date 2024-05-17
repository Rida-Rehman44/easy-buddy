from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='events_list'),
    path('create/', views.event_create, name='events_create'),
    path('edit/<int:event_id>/', views.event_edit, name='events_edit'),
]