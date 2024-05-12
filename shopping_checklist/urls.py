from django.urls import path
from .views import home, CreateView, EditView, DeleteView

app_name = 'shopping_checklist'

urlpatterns = [
    path('', home, name='shopping-list-home'),
    path('create/', CreateView.as_view(), name='create_shopping_checklist'),
    path('edit/<int:checklist_id>/', EditView.as_view(), name='edit_checklist'),
    path('delete_checklist/<int:checklist_id>/', DeleteView.as_view(), name='delete_checklist'),

]