# login/views.py
from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return HttpResponse("Hello World. You're at the login index")

# Create your views here.
def login(response):
    return HttpResponse("whatdup do")

def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid:
            form.save()
        return redirect("/home")
    else:
        form = UserCreationForm
    return render(response, "register/register.html", { "form": form })