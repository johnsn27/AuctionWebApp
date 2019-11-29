from datetime import datetime
from django.db.models import Max
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, QueryDict
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone

from .forms import PostItemForm, SignUpForm
from .models import SiteUsers, Item, Bid


class HomePageView(ListView):
    model = Item
    template_name = 'get_items.html'


class ExpiredView(ListView):
    model = Item
    template_name = 'expired_list.html'


@method_decorator(login_required, name='dispatch')
class SellView(CreateView):
    model = Item
    form_class = PostItemForm
    template_name = 'sell_item.html'
    success_url = 'sell'


@method_decorator(login_required, name='dispatch')
class WonView(ListView):
    model = Item
    template_name = 'won_items.html'

    def get_context_data(self, **kwargs):
        context = super(WonView, self).get_context_data(**kwargs)
        context['siteusers'] = SiteUsers.objects.values()
        context['items'] = Item.objects.values()
        context['bids'] = Bid.objects.values()
        return context


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


@method_decorator(login_required, name='dispatch')
class BuyView(TemplateView):
    template_name = 'buy_items.html'

    def get_context_data(self, **kwargs):
        context = super(BuyView, self).get_context_data(**kwargs)
        context['siteusers'] = SiteUsers.objects.values()
        context['items'] = Item.objects.values()
        context['bids'] = Bid.objects.values()
        return context


def items_json(request):
    if (request.method == 'GET'):
        query = request.GET.get('query')
        expired = request.GET.get('expired')
        bids = list(Bid.objects.values())
        users = list(SiteUsers.objects.values())
        if (expired):
            items = Item.objects.filter(endDate__lt=timezone.now())
        else:
            items = Item.objects.filter(endDate__gt=timezone.now())
        if (query):
            return JsonResponse({
                'items': list(Item.objects.filter(
                    Q(endDate__gt=timezone.now()),
                    Q(title__icontains=query) | Q(description__icontains=query)
                ).values()),
                'bids': bids,
                'users': users
            })
        else:
            return JsonResponse({
                'items': list(items.values()),
                'bids': bids,
                'users': users
            })
    else:
        return HttpResponseNotAllowed(['GET'])


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


@login_required
def viewProfile(request):
    context = {
        'user': request.user
    }
    return render(request, 'profile.html', context)


def editBid(request):
    if request.method == 'PUT':
        pk = QueryDict(request.body).get('item')
        bid = Bid.objects.filter(item_id=pk).order_by('price').last()
        oldPrice = 0
        if bid != None:
            oldPrice = bid.price
        finalPrice = oldPrice
        newPrice = float(QueryDict(request.body).get('price'))
        if newPrice > oldPrice:
            userId = QueryDict(request.body).get('userid')
            user = SiteUsers.objects.get(id=userId)
            item = Item.objects.get(pk=pk)
            b = Bid(price=newPrice, user=user, item_id=pk)
            b.save()
            finalPrice = newPrice
            error = None
        else:
            error = 'Bid is lower than current price'
        return JsonResponse({
            'price': finalPrice,
            'error': error
        })
    return HttpResponse("Not a PUT request")
