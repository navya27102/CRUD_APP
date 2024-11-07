from django.shortcuts import render,redirect
from .models import Employee
from django.contrib import messages

# Create your views here.
def index(request):
    data=Employee.objects.all()
    print(data)
    context={"data":data}
    return render(request,"index.html",context)

def insertdata(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        age=request.POST.get('age')
        position=request.POST.get('position')
        print(name,phone,age,position)
        query = Employee(name=name,phone=phone,age=age,position=position)
        query.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect("/")
    return render(request,"index.html")
    
def updateData(request,id):
    if request.method == 'POST':
        name=request.POST['name']
        phone=request.POST['phone']
        age=request.POST['age']
        position=request.POST['position']
        
        edit = Employee.objects.get(id=id)
        edit.name=name
        edit.phone=phone
        edit.age=age
        edit.position=position
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect("/")
    d = Employee.objects.get(id=id)
    context = {"d":d}
    return render(request,"edit.html",context)
def deleteData(request,id):
    d = Employee.objects.get(id=id)
    d.delete()
    messages.error(request,"Data Deleted Successfully")
    return redirect("/")