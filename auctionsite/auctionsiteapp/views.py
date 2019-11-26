from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import SiteUsers, Item
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import PostItemForm
from .models import Item
from auctionsiteapp.forms import SignUpForm

class HomePageView(ListView):
    model = Item
    template_name = 'get_items.html'

class CreatePostView(CreateView):
    model = Item
    form_class = PostItemForm
    template_name = 'post_item.html'
    success_url = reverse_lazy('')

def start(request):
    users = SiteUsers.objects.order_by('-id')[:5]
    context = {
        'posts': users,
    }
    return render(request, 'start.html', context)

def signup(request):
    users = SiteUsers.objects.order_by('-id')[:5]
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'start.html', {'users': users})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def getUser(request):
    users = SiteUsers.objects.order_by('-id')[:5]
    context = {
        'users': users,
    }
    return render(request, 'get_users.html', context)

def createUser(request):
    users = SiteUsers.objects.order_by('-id')[:5]
    context = {
        'users': users,
    }
    if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return render(request, 'start.html', {'users': users})
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def viewListings(request):
    items = Item.objects.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'listings.html', {'items': items})
