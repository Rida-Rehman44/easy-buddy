from django.urls import path
from . import views
app_name = 'groups'
urlpatterns = [
    path('create/', views.create_group, name='create_group'),  # URL pattern for creating a group
    path('search/', views.search_group, name='search_group'),  # URL pattern for searching groups
    path('join/<int:group_id>/', views.join_group, name='join_group'),  # URL pattern for joining a group
    path('home/', views.home, name='home'),
    path('google_home/', views.home, name='home'),
    path('group_detail/<int:group_id>/', views.group_detail, name='group_detail'),
    path('home_list', views.home_list_view,name='home_list'), # Adjust the view name as needed
    path('create_shopping_checklist/', views.create_shopping_checklist, name='create_shopping_checklist'),
    path('create_bulletin_board_message/', views.create_bulletin_board_message, name='create_bulletin_board_message'),
    path('bulletin_board/<int:group_id>/', views.bulletin_board_view, name='bulletin_board'),
    path('list/',views.list,name='list'),
    path('add/',views.add,name='add'),
    path('delete/',views.delete,name='delete'),
    path('edit/<int:checklist_id>/', views.EditView.as_view, name='edit_checklist'),
]

