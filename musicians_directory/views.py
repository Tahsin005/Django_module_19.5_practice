from django.shortcuts import render, redirect
from musician.models import Musician
from album.models import Album
def home(request):
    # musicians = Musician.objects.all()
    albums = Album.objects.all()
    return render(request, 'home.html', {'albums': albums})