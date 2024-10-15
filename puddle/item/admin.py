from django.contrib import admin
from item import models

# Register your models here.

class CatrgoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

class ItemAdmin(admin.ModelAdmin):
    list_display = ["name"]
    
   

admin.site.register(models.Category, CatrgoryAdmin)
admin.site.register(models.Item, ItemAdmin)
