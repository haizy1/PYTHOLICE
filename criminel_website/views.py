
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

# Create your views here.


def home1(request):
	return render(request, 'criminel_website/home1.html', {})
def home(request):
    return render(request, 'events/home.html', {})
def criminels_view(request):
    return render(request, 'criminels/criminels.html', {})
def alertes_view(request):
    return render(request, 'alertes/alertes.html', {})
def basededonnées_view(request):
    return render(request, 'basededonnées/basededonnées.html')




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


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username , password=password)
            login(request, user)
            messages.success(request, ("Registeration successfull"))
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'criminel_website/register_user.html',{
        "form":form,
        })

    

