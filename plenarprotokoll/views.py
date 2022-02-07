from django.shortcuts import render
from plenarprotokoll.models import Plenarprotokoll, Metaprotokoll

# Create your views here.
def plenarprotokoll_overview(request):
    metaprotokoll = Metaprotokoll.objects.all()
    context = {
        'metaprotokoll': metaprotokoll
    }
    return render(request, 'plenarprotokoll_overview.html', context)

def plenarprotokoll_index(request, sitzungsnr):
    plenarprotokoll = Plenarprotokoll.objects.filter(sitzungsnr=sitzungsnr)
    context = {
        'plenarprotokoll': plenarprotokoll
    }
    return render(request, 'plenarprotokoll_index.html', context)

def plenarprotokoll_detail(request, pk, sitzungsnr):
    plenarprotokoll_detail = Plenarprotokoll.objects.get(pk=pk, sitzungsnr = sitzungsnr)
    context = {
        'plenarprotokoll_detail': plenarprotokoll_detail
    }
    return render(request, 'plenarprotokoll_detail.html', context)