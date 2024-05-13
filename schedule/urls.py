from django.urls import path
from . import views


app_name = 'schedule'
# domain.com/schedule/delete

urlpatterns = [
    path('list/',views.list,name='list'),
    path('add/',views.add,name='add'),
    path('delete/',views.delete,name='delete'),
    
]


