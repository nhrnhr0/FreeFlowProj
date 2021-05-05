from django.contrib import admin

# Register your models here.
from .models import FreeFlowStores
class FreeFlowStoresAdmin(admin.ModelAdmin):
    list_display= ('name', 'url', 'img', 'lat', 'lng')
admin.site.register(FreeFlowStores, FreeFlowStoresAdmin)

