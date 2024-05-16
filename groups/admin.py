from django.contrib import admin

from .models import *

admin.site.register(Group)
admin.site.register(Artist)
admin.site.register(ShoppingChecklist)
admin.site.register(GroupCalendar)
admin.site.register(BulletinBoardMessage)
admin.site.register(BulletinBoards)
 ###
# Register your models here.
