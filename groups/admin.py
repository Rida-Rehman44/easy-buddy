from django.contrib import admin

from .models import *

admin.site.register(Group)
admin.site.register(Artist)
admin.site.register(ShoppingChecklist)

# Register your models here.
