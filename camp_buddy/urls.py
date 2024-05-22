from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apimodule.urls')),
    path('', include('users.urls')),
    path('', include('trip.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('bulletin_board.urls')),
    path('weatherapi/', include('weatherapi.urls')),
    path('', include('trip_calendar.urls')),
    path('', include('shopping_checklist.urls')),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
