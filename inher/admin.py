from django.contrib import admin
from inher.models import student,tech,nontech
# Register your models here.

class studentadmin(admin.ModelAdmin):
    list_display=['id','name','age','phone','email','course','fee','batch']
admin.site.register(student,studentadmin)

class techadmin(admin.ModelAdmin):
    list_display=['id','name','age','phone','email','sub','design','sal']
admin.site.register(tech,techadmin)

class nontechadmin(admin.ModelAdmin):
    list_display=['id','name','age','phone','email','design','sal']
admin.site.register(nontech,nontechadmin)