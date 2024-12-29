from django.contrib import admin
from .models import BrandModel ,OrderModel,Car_Model,Comment

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ['name', 'slug']


admin.site.register(BrandModel,BrandAdmin)
admin.site.register(Car_Model)
admin.site.register(OrderModel)
admin.site.register(Comment)


    
