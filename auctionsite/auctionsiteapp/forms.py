from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime 
from .models import Item

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    dateOfBirth = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = User
        fields = ('username', 'email', 'dateOfBirth', 'password1', 'password2')

class PostItemForm(forms.ModelForm):
    endDate = forms.DateField(initial=datetime.date.today)
    class Meta:
        model = Item
        fields = ['title', 'description', 'picture', 'endDate']