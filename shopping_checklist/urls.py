from django.urls import path
from .views import home, CreateView, EditView

urlpatterns = [
    path('', home, name='shopping-list-home'),
    path('create/', CreateView.as_view(), name='create_shopping_checklist'),
    path('edit/<int:checklist_id>/', EditView.as_view(), name='edit_checklist'),

]
