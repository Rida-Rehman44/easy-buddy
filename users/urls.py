from django.urls import path
from . import views
from users.views import loginview, registerview, logoutview, landingpage
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    

    path('', landingpage, name='landingpage'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-out/', views.sign_out, name='sign_out'),
    path('auth-receiver/', views.auth_receiver, name='auth_receiver'),
    #path('register/', views.register, name='register'),

    # calender changes
    path('login/', loginview, name='user_login'),
    path('register-user/', views.register, name='login'),
    path('register/', views.register, name='register'),
    path('account/password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),
    path('account/password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),
    path('account/password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('account/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('account/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('account/reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
    path('logout/', logoutview, name='logout'),
]


