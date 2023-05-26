from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Donation, User, Donator
from .form import MyUserCreationForm, DonationForm, DonatorForm

# Create your views here.
def home(request):
    donations = Donation.objects.order_by('-collected')[:3]

    context = {
        'donations': donations,
    }
    return render(request, 'base/index.html', context)

def list_donasi(request):
    donations = Donation.objects.all()
    context = {
        'donations': donations,
    }

    return render(request, 'base/list-donasi.html', context)

def donasi(request, pk):
    donation = Donation.objects.get(id=pk)
    top_donator = donation.donator_set.order_by('amount').first()
    latest_donator = donation.donator_set.order_by('-created').first()
    print(latest_donator)


    context = {
        'donation': donation,
        'top_donator': top_donator,
        'latest_donator': latest_donator,

    }

    return render(request, 'base/donasi.html', context)

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


@login_required(login_url='login')
def form_donation(request, pk):
    donation = Donation.objects.get(id=pk)
    form = DonatorForm()

    if request.method == 'POST':
        form = DonatorForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.donation = donation
            form.save()
            print(f'ID:\t{form.id}')
            return redirect(reverse('payment', kwargs={'pk1':donation.id, 'pk2':form.id}))

    context = {
        'donation': donation,
        'form': form,
    }

    return render(request, 'base/form-donasi.html', context)


def payment_success(request, pk1, pk2):

    donation = Donation.objects.get(id=pk1)
    donator = donation.donator_set.get(id=pk2)

    donator.paid = True
    donator.save()
    donation.collected += donator.amount
    donation.save()

    context = {
        'donator': donator,
    }
    return render(request, 'base/payment-success.html', context)


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

@login_required()
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