from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from constant import (USERNAME, EMAIL , PASSWORD_1 , PASSWORD_2, IMAGE)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = [USERNAME , EMAIL , PASSWORD_1 , PASSWORD_2]
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [USERNAME,EMAIL]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [IMAGE]


