from django.contrib import admin
from single.models import person,details
# Register your models here.

class personadmin(admin.ModelAdmin):
    list_display=['id','name','phone','email','dno','street','state','country','pin']
admin.site.register(person,personadmin)

class detailsadmin(admin.ModelAdmin):
    list_display=['id','name','phone','email']
admin.site.register(details,detailsadmin)