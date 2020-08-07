from django import forms 
from .models import UserRegistration
from .models import UserLogin

class UserRegForm (forms.ModelForm):
    class Meta:
        model = UserRegistration 
        fields = ['User Name', 'Email Address', 'Password']

class UserLoginForm (forms.ModelForm):
    class Meta:
        model = UserLogin
        fields = ['User Name', 'Password']
