from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def criminels_view(request):
    return render(request, 'criminels/criminels.html')
def alertes_view(request):
    return render(request, 'alertes/alertes.html', {})
def home(request):
    return render(request, 'events/home.html', {})
def basededonnées_view(request):
    return render(request, 'basededonnées/basededonnées.html')
def home1(request):
	return render(request, 'criminel_website/home1.html', {})
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "There was an Error Logging in! Try again")
            return redirect('login')
    else:
        return render(request, 'criminel_website/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were loged out!"))
    return redirect('home1')