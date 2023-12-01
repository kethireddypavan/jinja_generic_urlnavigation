from django.shortcuts import render

# Create your views here.
def customer1(request):
    return render(request,'customer1.html')

def salesman1(request):
    return render(request,'salesman1.html')

def customer2(request):
    return render(request,'customer2.html')

def salesman2(request):
    return render(request,'salesman2.html')

def customer3(request):
    return render(request,'customer3.html')

def salesman3(request):
    return render(request,'salesman3.html')


