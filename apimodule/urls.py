from django.urls import path
from .views import CreateDogs, DogList, ListCreat, DoggetUpdateDelete

urlpatterns = [
    path('api/create_dogs/', CreateDogs.as_view(), name='create-dogs'),
    path('api/dog_list/', DogList.as_view(), name='dog-list'),
    path('api/edit_dogs/', CreateDogs.as_view(), name='edit-dogs'),
    path('api/delete_dogs/<int:pk>', CreateDogs.as_view(), name='delete-dogs'),
    path('api/update_dogs/<int:pk>', CreateDogs.as_view(), name='update-dogs'),
    path('api/underdog/', ListCreat.as_view(), name='underdog'),
    path('api/topdog/<int:pk>', DoggetUpdateDelete.as_view(), name='topdog'),

]
