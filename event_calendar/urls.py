from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('auth/', views.auth, name='auth'),
    path('auth/callback/', views.auth_callback, name='auth_callback'),
]
