from django.contrib import admin
from prox.models import proxyemployee,employee
# Register your models here.
class employeeadmin(admin.ModelAdmin):
    list_display=['id','name','sal','dept','mtr']

admin.site.register(employee,employeeadmin)

class proxyemployeeadmin(admin.ModelAdmin):
    list_display=['id','name','sal','dept','mtr']

admin.site.register(proxyemployee,proxyemployeeadmin)