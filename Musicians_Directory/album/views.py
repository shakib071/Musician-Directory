from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import AlbumModel

# Create your views here.


def add_album(request):
    
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_album")
        
    else:
        form = AlbumForm()
    return render(request,'add_album.html',{'form':form})

