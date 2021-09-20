from django.contrib import messages
from django.shortcuts import render,redirect
from .fakers import *
from .models import Student
from django.core.paginator import Paginator


# Create your views here.

def Populate_view(request):
    if request.method =='POST':
        n=request.POST.get('data')
        np=int(n)
        for i in range(np):
            frollno=randint(1,500)
            fname=faker.name()
            faddress=faker.address()
            fmarks=randint(1,100)
            stu_records=Student.objects.get_or_create(rollno=frollno,name=fname,address=faddress,marks=fmarks)
        messages.success(request,'Data insurted Successfully')
    templates_name='fakerdata.html'
    return render(request,templates_name)

def Pagination_show_view(request):
    stu=Student.objects.all()
    paginator=Paginator(stu,10)
    page_no=request.GET.get('page',1)
    obj=paginator.get_page(page_no)
    template_name='pagination.html'
    context={'obj':obj}
    return render(request,template_name,context)