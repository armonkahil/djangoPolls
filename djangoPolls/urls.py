"""djangoPolls URL Configuration

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
from django.urls import include, path
from login import views as v
from main import views as m
from polls import views as p

urlpatterns = [
    path('login/', include('login.urls')),
    path('register/', v.register, name="register"),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('home/', include('main.urls')),
    path('', include('main.urls')),
]
