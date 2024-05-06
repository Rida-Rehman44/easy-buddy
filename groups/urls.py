from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_group, name='create_group'),  # URL pattern for creating a group
    path('search/', views.search_group, name='search_group'),  # URL pattern for searching groups
    path('join/<int:group_id>/', views.join_group, name='join_group'),  # URL pattern for joining a group
    path('home/', views.home_view, name='home'),
]
