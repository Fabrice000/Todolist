from django.contrib import admin
from .models import Taches

# Register your models here.

class AdminTaches(admin.ModelAdmin):
    list_display = ('finish','name','description','priority','categories')
    
admin.site.register(Taches,AdminTaches)