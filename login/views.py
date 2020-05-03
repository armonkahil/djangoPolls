# login/views.py
from django.shortcuts import HttpResponse, render, redirect
from .forms import RegisterForm

def index(request):
    return HttpResponse("Hello World. You're at the login index")

# Create your views here.
def login(response):
    return HttpResponse("whatdup do")

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid:
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", { "form": form })