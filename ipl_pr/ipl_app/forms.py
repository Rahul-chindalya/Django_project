from django import forms
from django.contrib.auth.models import User
from .models import Players,Stadium,Profile

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Players
        fields = "__all__"


class StadiumForm(forms.ModelForm):

    class Meta:
        model = Stadium
        fields = '__all__'


class UserRegiterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email','password','confirm_password']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['phone','address','profile_photo']