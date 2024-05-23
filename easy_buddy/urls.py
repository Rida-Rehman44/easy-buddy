"""
URL configuration for easy_buddy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views 
from django.urls import path, include
from users.views import ChangePasswordView

from users.forms import LoginForm

from .views import HomeView

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('', HomeView.as_view(), name= "home"),

    path('home', include('users.urls')),

    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=LoginForm), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),


    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    
    
    path('schedule/',include('schedule.urls', namespace='schedule')),
    
    path('shopping_checklist/', include('shopping_checklist.urls'), name='shopping_checklist'),
    
    path('events/', include('events.urls'), name='events'),
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


