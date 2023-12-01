"""
URL configuration for project5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer1/',customer1,name='customer1'),
    path('salesman1/',salesman1,name='salesman1'),
    path('customer2/',customer2,name='customer2'),
    path('salesman2/',salesman2,name='salesman2'),
    path('customer3/',customer3,name='customer3'),
    path('salesman3/',salesman3,name='salesman3'),

]
