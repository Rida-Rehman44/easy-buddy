from django.urls import path
from .views import home, CreateView

urlpatterns = [
    path('', home, name='shopping-list-home'),
    path('create/', CreateView.as_view(), name='create_shopping_checklist'),
]
