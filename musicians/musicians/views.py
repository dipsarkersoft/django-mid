from django.shortcuts import render

from album.models import Album_model


def home(request):
    all_data=Album_model.objects.all()
    
    return render(request,'home.html',{'data':all_data})