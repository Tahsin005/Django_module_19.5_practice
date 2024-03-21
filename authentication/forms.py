from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"id": "required"})) 
    last_name = forms.CharField(widget=forms.TextInput(attrs={"id": "required"})) 
    email = forms.EmailField(widget=forms.EmailInput(attrs={"id": "required"})) 
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        

class EditProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        