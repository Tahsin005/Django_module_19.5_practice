from django.shortcuts import render, redirect
from musician.forms import MusicianForm
from musician.models import Musician
from django.contrib.auth.decorators import login_required

# Create your views here.
def create_musician(request):
    form = MusicianForm()
    if request.method == "POST":
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("home")
    return render(request, "create_musician.html", {"form": form})

def edit_musician(request, id):
    musician = Musician.objects.get(pk=id)
    form = MusicianForm(instance=musician)
    if request.method == "POST":
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save(commit=True)
            return redirect("home")
        
    return render(request, "create_musician.html", {"form": form})

def delete_musician(request, id):
    musician = Musician.objects.get(pk=id)
    musician.delete()
    return redirect("home")