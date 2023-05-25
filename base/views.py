from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Donation, User
from .form import MyUserCreationForm, DonationForm

# Create your views here.
def home(request):
    donations = Donation.objects.order_by('-collected')[:3]
    print(donations)

    context = {
        'donations': donations,
    }
    return render(request, 'base/index.html', context)

def list_donasi(request):
    donasions = Donation.objects.all()
    context = {
        'donasions': donasions,
    }

    return render(request, 'base/list-donasi.html', context)

def kategori(request):
    context = {

    }

    return render(request, 'base/kategori.html', context)

@login_required(login_url='login')
def form_galang_dana(request):

    form = DonationForm()

    if request.method == "POST":
        form = DonationForm(request.POST, request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'base/form-galang-dana.html', context)


def login_page(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'email or password does not exist')

    context = {
        'page': 'login',
    }

    return render(request, 'base/login-register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def register_page(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.email = user.email.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {
        'form': form,
        'page': 'register',
    }

    return render(request, 'base/login-register.html', context)