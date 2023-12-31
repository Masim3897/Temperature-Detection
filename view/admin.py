from django.contrib import admin
from view.models import Temprature

class TempratueAdmin(admin.ModelAdmin):
    list_display = ('name','value')

admin.site.register(Temprature,TempratueAdmin)

# Register your models here.
