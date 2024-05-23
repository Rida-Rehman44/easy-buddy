from django.urls import path
from .views import list_home, CreateView, EditView, DeleteView

urlpatterns = [
    path('list_home/', list_home, name='list_home'),
    path('create_list/', CreateView.as_view(), name='create_shopping_checklist'),
    path('edit_list/<int:checklist_id>/', EditView.as_view(), name='edit_checklist'),
    path('delete_list/<int:checklist_id>/', DeleteView.as_view(), name='delete_checklist'),

]