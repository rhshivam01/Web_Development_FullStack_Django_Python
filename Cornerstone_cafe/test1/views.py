from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from .models import Products, contact_query
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate , login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def home(request):
    product_info = Products.objects.all()
    print(product_info)
    return render(request, 'test1/home.html', {'product_info': product_info})
    #return HttpResponse('Home Page')
    
def findproduct(request):
    if request.method == 'POST':
        x = request.POST.get('prod_search')
        print(x)
        mydata = Products.objects.filter(
            Q(product_name__icontains=x) | Q(product_category__icontains=x) | Q(product_id__icontains=x)
        )
        print(mydata)
        return render(request, 'test1/products.html', {'products_info': mydata})
    else:
        return render(request, 'test1/products.html', {'products_info': Products.objects.all()})
    
            

def contact(request):
    if request.method == 'GET':
        return render(request, 'test1/contact.html')
    else:
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('phone')
        print(a, b, c)
        new_data = contact_query(name=a, email=b, phone=c)
        new_data.save()
        return render(request, 'test1/contact.html',{'x': 'Message Sent Successfully'})
    #return HttpResponse('Contact Details')

def about(request):
    return render(request,'test1/about.html')
    #return HttpResponse('About Us')

@login_required(login_url='login')
def products(request):
    product_info = Products.objects.all().order_by('id')
    pagenation = Paginator(product_info, 3)   
    page_number = request.GET.get("page")
    page_obj = pagenation.get_page(page_number)
    return render(request, 'test1/products.html',{'page_obj': page_obj})
    #return HttpResponse('Products Page')
    
def login(request):
    if request.method == "GET":
        return render(request, 'test1/login.html', {'form': AuthenticationForm()})
    else:
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'test1/login.html', {'form': AuthenticationForm(), 'error': 'Invalid credentials'})
        else:
            auth_login(request , user)
            return redirect('home')
        
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('contact', '').strip()
        password1 = request.POST.get('password1', '').strip()
        password2 = request.POST.get('password2', '').strip()
        print(password1, password2, username, email, phone)

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        auth_login(request, user)  
        return redirect('home')  
    else:
        return render(request, 'test1/signup.html')
    
    
def logout(request):
    if request.method == "GET":
        logout(request)
        return redirect('home')