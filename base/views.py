from django.shortcuts import render
from .models import Donation

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