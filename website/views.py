from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from django.contrib.auth.forms import UserCreationForm
from .models import Record

# Create your views here.

def home(request):
     records = Record.objects.all()
   
     #check to see if loggin
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']  
     #Authenticate
        user = authenticate(request, username= username, password = password)
        if user is not None:
         login(request,user)  
         messages.success(request,"You have been successfully logged in!")
         return redirect('home')
        else:
           messages.success(request,"There was an error logging in.Please try again...")
           return redirect('home')
     else:    
        return render(request,'home.html',{'records':records }) 



def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out successfully...")
    return redirect('home')

def register_user(request):
   if request.method == 'POST':
       form = SignUpForm(request.POST)
       if form.is_valid():
             form.save()
        
           #Authenticate and login
             username = form.cleaned_data['username']
             password = form.cleaned_data['password1']
             user = authenticate(username= username, password= password)
             login(request, user)
             messages.success(request, "You have successfully registered...")
             return redirect('home')
   else:
        form = SignUpForm()    
        return render(request,'register.html',{'form':form}) 
    
   return render(request,'register.html',{'form':form})   

def Register_User(request):
   if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
           form.save() 
           username = form.cleaned_data['username']
           password = form.cleaned_data['password1']
           user = authenticate(username=username, password=password)
           login(request, user)
           messages.success(request, "You have successfully registered...")
           return redirect('home')

   else:
        form = UserCreationForm()   

   return render(request,"authenticate/Register_User.html",{'form':form,})


def Record_customer(request, pk):
   if request.user.is_authenticated: 
     #look up record
     Record_customer = Record.objects.get(id=pk)
     return render(request,'Record.html',{'Record_customer': Record_customer })  
   else:
       messages.success(request, "You must be logged in to view this page")
       return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "You record has been deleted successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete record...")
        return render(request,'Record.html',{'delete_it': delete_it })
    
def add_record(request):
       form = AddRecordForm(request.POST)
       if request.user.is_authenticated:
           if request.method == "POST":
                  if form.is_valid():
                   add_record = form.save()
                   messages.success(request, "You record has been saved successfully")
                   return redirect('home')
           return render(request,'add_record.html',{'form':form}) 
       else: 
           messages.success(request, "You must be logged in to add record...")
           return redirect('home')
       

def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "You record has been updated successfully")
            return redirect('home')
        return render(request,'update_record.html',{'form': form })
    else:
        messages.success(request, "You musted be logged in...")
        return redirect('home')





