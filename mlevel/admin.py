from django.contrib import admin
from mlevel.models import bank,bank1,bank2
# Register your models here.

class bankadmin(admin.ModelAdmin):
    list_display=['id','name','age','address']
admin.site.register(bank,bankadmin)

class bank1admin(admin.ModelAdmin):
    list_display=['id','name','age','address','pan','phone']
admin.site.register(bank1,bank1admin)

class bank2admin(admin.ModelAdmin):
    list_display=['id','name','age','address','pan','phone','adhaar','email']
admin.site.register(bank2,bank2admin)