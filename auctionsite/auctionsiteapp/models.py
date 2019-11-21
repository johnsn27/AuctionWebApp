from django.db import models
from django import forms

# from django.contrib.auth.models import BaseUserManager

# class UserManager(BaseUserManager):

#     def create_user(self, username, email, password, dob):
#         if not username:
#             raise ValueError('The given username must be set')
#         email = self.normalize_email(email)
#         username = self.model.normalize_username(username)
#         dob = self.
#         user = self.model(username=username, email=email, dob=dob)
#         user.set_password(password)

class User(models.Model, forms.ModelForm):
    email = models.EmailField()
    dateOfBirth = model.DateTimeField()
    password = forms.CharField(widget=forms.PasswordInput)

class Item(models.Model):
    title = models.TextField()
    description = models.TextField()
    picture = models.ImageField(upload_to='images/')
    endDate = model.DateTimeField()
