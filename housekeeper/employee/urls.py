"""housekeeper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from django.contrib import admin
from django import views
from django.urls import path
from employee.views import *
from employee import views
from django.contrib import admin
urlpatterns = [
    path('login/', Userlogin.as_view(), name='userlogin'),
    path('profile/', profileview.as_view(), name='profilepage'),
    path('register/',BaseRegisterView.as_view() , name='add_employee'),
    path('view/', Listemployee.as_view(), name='list_employee'),
    path('<int:pk>delete/', Deleteemployee.as_view(), name='delete_employee'),
    path('<int:pk>update/', Updateemployee.as_view(), name='update_employee'),
    path("",views.IndexPage,name="index"),
    
]

