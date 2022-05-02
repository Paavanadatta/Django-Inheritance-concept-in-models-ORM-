from django.http import HttpResponse
from django.shortcuts import render
from student.models import studentmodel
# Create your views here.
def create(request,id,name,age,email,phone):
    studentmodel.objects.create(id=id,name=name,age=age,email=email,phone=phone)
    return HttpResponse("value is created")

def update(request,id,age,email,):
    studentmodel.objects.filter(id=id).update(age=age,email=email)
    return HttpResponse("value is updated")

def delete(request,id):
    studentmodel.objects.filter(id=id).delete()
    return HttpResponse("value is deleted")

def select(request):
    res=studentmodel.objects.all()
    return render(request,"select.html",{'res':res})

