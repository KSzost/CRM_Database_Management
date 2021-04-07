from django.contrib import admin

from .models import *

class RulesAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Rules)
admin.site.register(Trades)
admin.site.register(Users)
admin.site.register(Companies)
admin.site.register(Notes)
admin.site.register(Contact)

