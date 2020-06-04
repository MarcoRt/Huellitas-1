"""Huellitas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Huellitas.views import index, products, login, user_register, dates, appointment, param_num

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('productos/', products),
    path('login/', login),
    path('registro/', user_register),
    path('citas/', dates),
    path('agendar/', appointment),
    # Ejemplo URL con dos parámetros numéricos
    path('suma/<int:num1>/<int:num2>/', param_num),
]