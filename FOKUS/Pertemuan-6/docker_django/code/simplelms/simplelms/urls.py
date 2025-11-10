"""
URL configuration for simplelms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# code/simplelms/simplelms/urls.py

from django.contrib import admin
from django.urls import path, include  # <-- Wajib ada 'include'
from core import views as core_views  # <-- Wajib ada jika ingin home view

urlpatterns = [
    # Path untuk home view (mengatasi 404 pada root /)
    path('', core_views.home, name='home'), 
    
    path('admin/', admin.site.urls),
    
    # BARIS INI WAJIB AGAR /core/ BISA DIAKSES
    path('core/', include('core.urls')), 
]