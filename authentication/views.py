from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

from authentication.forms import RegistrationForm, EditProfileForm
# Create your views here.

def signup(request):
    if not request.user.is_authenticated:
        form = RegistrationForm()
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                form.save(commit=True)
                return redirect('login')
        return render(request,'signup.html', {'form': form})
    else:
        return redirect('profile')
    
def user_login(request):
    if not request.user.is_authenticated:
        form = AuthenticationForm()
        if request.method == 'POST':
            form = AuthenticationForm(request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name, password=userpass)
                
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successuflly')
                    return redirect('profile')
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('home')
    
def user_logout(request):
    logout(request)
    return redirect('login')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect("login")
    

def pass_change1(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            update_session_auth_hash(request, form.user) 
            messages.success(request, "Password changed.")
            return redirect("profile")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'reset_pass.html', {'form': form})


def pass_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password changed.")
            return redirect("profile")
    else:
        form = SetPasswordForm(request.user)
    return render(request, 'reset_pass.html', {'form': form})


def edit_profile(request):
    if request.user.is_authenticated:
        form = EditProfileForm(instance= request.user)
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=request.user)
            
            if form.is_valid():
                messages.success(request, 'Information changed successfully!')
                form.save(commit=True)
                return redirect("profile")
        return render(request, 'edit_profile.html', {"form": form})
    else:
        return redirect("login")