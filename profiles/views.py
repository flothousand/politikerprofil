from django.shortcuts import render
from profiles.models import Profiles

# Create your views here.

def profiles_index(request):
    profiles = Profiles.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'profiles_index.html', context)

def profiles_detail(request, pk):
    profiles = Profiles.objects.get(pk=pk)
    context = {
        'profiles': profiles
    }
    return render(request, 'profiles_detail.html', context)