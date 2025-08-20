from django.shortcuts import render,redirect
from album.models import AlbumModel
def home(request):
    album_list = AlbumModel.objects.all()
    return render(request,'home.html',{'album_list': album_list})