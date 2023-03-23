from django.shortcuts import render, HttpResponse
from .models import BannerWeb, Icons

def home(request):
    banner = BannerWeb.objects.all()
    icon_pengelolaan_pbj = Icons.objects.get(judul='pengelolaanpbj')
    icon_lpse = Icons.objects.get(judul='lpse')
    icon_sdm = Icons.objects.get(judul='sdm')
    context = {
        'pictures': banner,
        'icon1': icon_pengelolaan_pbj,
        'icon2': icon_lpse,
        'icon3': icon_sdm,
    }
    return render(request, 'blog/home_blog.html', context)
   
