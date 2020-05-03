# login/views.py
from django.shortcuts import HttpResponse, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return HttpResponse("Hello World. You're at the login index")

# Create your views here.
def login(response):
    return HttpResponse("whatdup do")

def register(response):
    form = UserCreationForm
    return render(response, "register/register.html", { form: form })