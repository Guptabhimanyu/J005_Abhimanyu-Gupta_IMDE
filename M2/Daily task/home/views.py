from ast import IsNot
from asyncio import Task
from .forms import TaskForms
from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Task




def home(request):
    try:
        data=Task.objects.filter(user=request.user.id)
        print(data)
        context={"data":data}   
    except :
        messages.warning(request,"Nothing found")
        return redirect('view')
    return render(request,'index.html')

@login_required(login_url='login')
def DailyTask(request):
    try:
        data = Task.objects.all()
        context = {"Task": data}
    except Exception as e:
        context = {"Task": "data not found" }
    return render(request, 'dailytask.html', context)

def TaskAdd(request): 
    form = TaskForms()
    if request.method == 'POST':
        myData = TaskForms(request.POST)
        if myData.is_valid():
            myData.save()
            messages.success(request, 'Project Added Successfully!!')
            return redirect('projects')
    context={"form":form}
    return render(request, 'taskAdd.html', context)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['Name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
      
        
        if user is not None:
            login(request, user)
            return redirect('projects')
        
        else:
            print("The sign in detail doesn't exist")
            return redirect('signup')
        

    return render(request, 'login.html')

@login_required(login_url='login')
def logoutpage(request):
    print("You Have Successfully Logged Out")
    logout(request)
    return redirect('home') 

@login_required(login_url='login')
def taskDelete(request, id):
    data = Task.objects.get(id=id)
    data.delete()
    messages.warning(request, 'Project has been deleted!!')
    return redirect('projects')

@login_required(login_url='login')
def taskDetails(request, ag):
    # fetchData = Project.objects.filter(name=ag)
    # print(fetchData.query)
    # print(fetchData)  
    fetchData = Task.objects.get(name=ag)
    context = {"fetchData":fetchData}
    return render(request,'taskDetail.html', context)

@login_required(login_url='login')
def taskUpdate(request,id):
    mydata = Task.objects.get(id=id)
    updateForm  = TaskForms(request.POST or None ,instance = mydata)
    if updateForm.is_valid():
        updateForm.save()
        messages.success(request, 'Project Updated Successfully!!')
        return redirect('projects')
    context = {"form":updateForm}
    
    return render(request,'taskUpdate.html', context)


    
