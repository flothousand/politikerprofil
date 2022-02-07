from django.shortcuts import render

# Create your views here.
def impressum_overview(request):
    context = {
    }
    return render(request, 'impressum_overview.html', context)