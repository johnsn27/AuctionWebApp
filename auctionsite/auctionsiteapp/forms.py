from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime
from .models import Item

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required. Provide a valid email address.')
    dateOfBirth = forms.DateField(initial=datetime.date.today, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'email', 'dateOfBirth', 'password1', 'password2')

class PostItemForm(forms.ModelForm):
    endDate = forms.DateField(initial=datetime.date.today)
    title = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 1}))
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 2}))

    class Meta:
        model = Item
        fields = ['title', 'description', 'picture', 'price', 'endDate']


