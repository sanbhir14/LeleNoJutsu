"""LeleNoJutsu URL Configuration

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
from django_cas_ng import views as cas_views
from master import views as masterViews
# from django.urls import path, re_path


urlpatterns = [
    path('', masterViews.landingPage, name="landingPage"),
    path('red/', masterViews.redirect, name='redirect'),
    path('admin/', admin.site.urls),
    path('login/', cas_views.LoginView.as_view(), name='login'),
    path('logout/', cas_views.LogoutView.as_view(), name='logout'),
    path('home/', masterViews.home, name="home"),
    path('input/', masterViews.input, name="input"),
]
