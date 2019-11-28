from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, QueryDict
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone

from .forms import PostItemForm, SignUpForm
from .models import SiteUsers, Item


class HomePageView(ListView):
    model = Item
    template_name = 'get_items.html'


class SearchView(ListView):
    model = Item
    template_name = 'item_search.html'


class ExpiredView(ListView):
    model = Item
    template_name = 'expired_list.html'


class SellView(CreateView):
    model = Item
    form_class = PostItemForm
    template_name = 'sell_item.html'
    success_url = reverse_lazy('')

class BuyView(ListView):
    model = Item
    template_name = 'buy-items.html'

    def get_context_data(self, **kwargs):
        context = super(BuyView, self).get_context_data(**kwargs)
        context['siteusers'] = SiteUsers.objects.all()
        context['items'] = Item.objects.all()
        return context

def items_json(request):
    if (request.method == 'GET'):
        query = request.GET.get('query')
        expired = request.GET.get('expired')
        if (expired):
            items = Item.objects.filter(endDate__lt=timezone.now())
        else:
            items = Item.objects.filter(endDate__gt=timezone.now())
        if (query):
            return JsonResponse({
                'items': list(Item.objects.filter(
                    Q(endDate__gt=timezone.now()),
                    Q(title__icontains=query) | Q(description__icontains=query)
                ).values())
            })
        else:
            return JsonResponse({
                'items': list(items.values())
            })
    else:
        return HttpResponseNotAllowed(['GET'])

def changeUsername(request):
    if (request.method == 'PUT'):
        newUsername = QueryDict(request.body).get('newUsername')
        user = User.objects.get(pk=request.user.id)
        try:
            User.objects.get(username=newUsername)
            raise ValidationError(('Username in use'), code='NAME_IN_USE')
        except User.DoesNotExist: 
            user.username = newUsername
            user.save()
            return JsonResponse({
                'username': user.username
            })

def start(request):
    return render(request, 'start.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            dateOfBirth = form.cleaned_data.get('dateOfBirth')
            SiteUsers.objects.create(user=user, dateOfBirth=dateOfBirth)
            login(request, user)
            return render(request, 'start.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def createUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'start.html')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def viewProfile(request):
    context = {
        'user': request.user
    }
    return render(request, 'profile.html', context)


def editBid(request):
    if request.method == 'PUT':
        pk = QueryDict(request.body).get('item')
        item = Item.objects.get(pk=pk)
        newPrice = float(QueryDict(request.body).get('price'))
        error = None
        if newPrice > item.price:
            item.price = newPrice
            item.save()
        else:
            error = 'Bid is lower than current price'
        return JsonResponse({
            'id': item.id,
            'price': item.price,
            'error': error
        })
    return HttpResponse("Not a PUT request")
