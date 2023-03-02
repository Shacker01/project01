from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import Clients
from .models import Treatment, Farmers, Products, Medicines, Plants
from .forms import TreatmentForm, FarmersForm, ProductsForm, MedicinesForm, PlantsForm



def splash(request):
    return render(request, 'splash.html')

@login_required(login_url = 'register')
def home(request):
    context = {}
    context['product'] = Products.objects.all()
    return render(request, 'home.html', context)

# account creation, login, logout, delete user account
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if Clients.objects.filter(username=username).exists():
                messages.error(request, 'Username taken')
                return redirect('register')
            elif Clients.objects.filter(email=email).exists():
                messages.error(request, 'Email exist')
                return redirect('register')

            else:
                client = Clients.objects.create(first_name=first_name, last_name=last_name, username=username)
                client.save()
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                messages.info(request,'user created')
                return redirect('login')

        else:
            messages.error( request, "Password don't match.")
            return redirect('register')
    else:
        return render(request, 'register.html')


def Login(request):
    if request.method=='POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        user = auth.authenticate(username=username,password=password1)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'username or password incorrect!')
            return redirect('login')

    else:

        return render(request, 'Login.html')
    
    
def logout(request):
    auth.logout(request)
    return redirect('/')
    
    
def del_user(request, pk):
    client = User.objects.get(id=pk)
    client = Clients.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('/')
    context = {'client':client}
    return render(request, 'del_user.html', context)


def Farm(request):
    return render(request, 'farm.html')

# Items uploaded for sell
def Availability(request):
    context = {}
    context['product'] = Products.objects.all()
    return render(request, 'available.html', context) 


def Plant(request):
   
    if request.method == 'POST':
        form = PlantsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image_obj = form.instance
            return redirect('plant')

        else:
            form = PlantsForm()
    form = PlantsForm()
    # return render(request, 'plant.html', {'form':form})
    context = {'form':form}
    context['plant'] = Plants.objects.all()
    return render(request, 'plant.html', context) 

def Cultivation(request):
    return render(request, 'cultivation.html')

def Treatment(request):
    if request.method == 'POST':
        form = TreatmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image_obj = form.instance

        else:
            form = TreatmentForm()
    form = TreatmentForm()            
    return render(request, 'treatment.html', {'form':form})

def ContactUs(request):
    return render(request, 'contactUs.html')

def AboutUs(request):
    return render(request, 'aboutUs.html')

def FAQS(request):
    return render(request, 'faqs.html')

def Answers(request):
    return render(request, 'answers.html')

def Privacy(request):
    return render(request, 'privacy.html')


def Farmers(request):
    if request.method == 'POST':
        form = FarmersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image_obj = form.instance

        else:
            form = FarmersForm()
    form = FarmersForm()            
    return render(request, 'farmers.html', {'form':form})

@login_required(login_url = 'login')
def Product(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image_obj = form.instance
            return redirect("available")

        else:
            form = ProductsForm()
    form = ProductsForm()
    return render(request, 'product.html', {'form':form})

def Medicine(request):
    form = MedicinesForm()
    if request.method == 'POST':
        form = MedicinesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image_obj = form.instance
            return redirect('medicine')
        else:
            form = MedicinesForm()
    form = MedicinesForm()
    context = {'form':form}
    context['medicine'] = Medicines.objects.all()  
    return render(request, 'medicine.html', context)
    
def UpdateDrugs(request):
    context = {}
    context['medicine'] = Medicines.objects.all()
    return render(request, 'medicine.html', context) 
    