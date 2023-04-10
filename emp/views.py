from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import Employee1
from django.db.models import Q 
# Create your views here.

def index(request):
    return render(request , "index.html" ,{})

def all_emp(request):
    emps = Employee1.objects.all()
    return render(request , "all_emp.html" ,{"emps": emps})

def add_emp(request):
    if request.method=="POST":

        #data fetch
        emp_first_name = request.POST.get("emp_first_name")
        emp_last_name = request.POST.get("emp_last_name")
        emp_age = request.POST.get("emp_age")
        emp_department = request.POST.get("emp_department")
        emp_salary = request.POST.get("emp_salary")
        emp_bonus = request.POST.get("emp_bonus")
        emp_role = request.POST.get("emp_role")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")

        #Create model object and set the data

        e = Employee1()
        e.emp_first_name = emp_first_name
        e.emp_last_name = emp_last_name
        e.emp_age = emp_age
        e.emp_department = emp_department
        e.emp_salary = emp_salary
        e.emp_bonus = emp_bonus
        e.emp_role = emp_role
        e.emp_phone = emp_phone
        e.emp_address = emp_address
        if (emp_working == None):
            e.emp_working = False
        else:
            e.emp_working = True

        #save the object
        e.save()
        return redirect ("/all_emp")
    return render(request , "add_emp.html" ,{})

def del_emp(request , emp_id = 0):
    if emp_id:
        emp_removed = Employee1.objects.get(id = emp_id)
        emp_removed.delete()
        

    emps = Employee1.objects.all()
    return render(request , "del_emp.html" ,{"emps": emps})


def update_emp(request , emp_id):
    emps = Employee1.objects.get(pk = emp_id)
    return render(request , "update_emp.html" ,{"emps": emps})

def doUpdate_emp(request , emp_id):
    if request.method=="POST":

        #data fetch
        emp_first_name = request.POST.get("emp_first_name")
        emp_last_name = request.POST.get("emp_last_name")
        emp_age = request.POST.get("emp_age")
        emp_department = request.POST.get("emp_department")
        emp_salary = request.POST.get("emp_salary")
        emp_bonus = request.POST.get("emp_bonus")
        emp_role = request.POST.get("emp_role")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")

        #Create model object and set the data

        e = Employee1.objects.get(pk = emp_id)
        e.emp_first_name = emp_first_name
        e.emp_last_name = emp_last_name
        e.emp_age = emp_age
        e.emp_department = emp_department
        e.emp_salary = emp_salary
        e.emp_bonus = emp_bonus
        e.emp_role = emp_role
        e.emp_phone = emp_phone
        e.emp_address = emp_address
        if (emp_working == None):
            e.emp_working = False
        else:
            e.emp_working = True

        #save the object
        e.save()
        return redirect ("/all_emp")
    return render(request , "update_emp.html" ,{})


def filter_emp(request):
    if request.method == "POST":

        emp_name = request.POST.get("emp_first_name")
        emp_department = request.POST.get("emp_department")
        emp_role = request.POST.get("emp_role")
        emp_working = request.POST.get("emp_working")

        e = Employee1 ()
        e.emp_first_name = emp_name
        e.emp_department = emp_department
        e.emp_role = emp_role
       
        emps = Employee1.objects.all()

        if emp_name  :
            emps = emps.filter(Q(emp_first_name__icontains = emp_name) | Q(emp_last_name__icontains = emp_name)) 

        if emp_department :
            emps = emps.filter(Q(emp_department__icontains = emp_department))
        
        if emp_role :
            emps = emps.filter(Q(emp_role__icontains = emp_role))
        
        return render(request , "all_emp.html" , {"emps" : emps})

    elif request.method == "GET":
        return render(request , "filter_emp.html")

    else:
        return HttpResponse("An exception occured")




