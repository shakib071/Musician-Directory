from django.shortcuts import render,redirect,get_object_or_404
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



def edit_album(request,id):
    album = AlbumModel.objects.get(pk=id)
    album_form = AlbumForm(instance=album)
    # album = get_object_or_404(AlbumModel, id=id) 
    if request.method == "POST":
        album_form = AlbumForm(request.POST,instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
   
    return render(request,'add_album.html',{'form' : album_form})

def delete_album(request,id):
    album = AlbumModel.objects.get(pk=id)
    album.delete()
    return redirect('homepage')


