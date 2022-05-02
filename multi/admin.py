from django.contrib import admin
from multi.models import rbi,bank,bank1

# Register your models here.
class rbiadmin(admin.ModelAdmin):
    list_display=['id','name','age','address']
admin.site.register(rbi,rbiadmin)

class bankadmin(admin.ModelAdmin):
    list_display=['ifsc','si']
admin.site.register(bank,bankadmin)

class bank1admin(admin.ModelAdmin):
    list_display=['id','name','age','address','ifsc','si','pan','phone','adhaar','email']
admin.site.register(bank1,bank1admin)