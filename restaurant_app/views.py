from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request,'home.html')

def home_page1(request):
    return render(request,'home1.html')

def products(request):
    return render(request,'product.html')

def products1(request):
    return render(request,'product1.html')

def cart(request):
    return render(request,'cart.html')

def aboutus(request):
    return render(request,'about.html')

def aboutus1(request):
    return render(request,'about1.html')

def contactus(request):
    return render(request,'contact.html')

def contactus1(request):
    return render(request,'contact1.html')

def checkout(request):
    return render(request,'checkout.html')

def home(request):
    return render(request,'login.html')

def sign_up(request):
    return render(request,'sign_up.html')

def product_detail(request):
    return render(request,'product_detail.html')

def product_detail1(request):
    return render(request,'product_detail1.html')
