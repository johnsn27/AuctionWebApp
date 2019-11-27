from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, QueryDict
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
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


class CreatePostView(CreateView):
    model = Item
    form_class = PostItemForm
    template_name = 'post_item.html'
    success_url = reverse_lazy('')


class AuctionView(ListView):
    model = Item
    template_name = 'auction.html'


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
            dateOfBirth = form.cleaned_data.get('dateOfBirth')
            SiteUsers.objects.create(user=user, dateOfBirth=dateOfBirth)
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
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'listings.html', {'items': items})


def viewProfile(request):
    context = {
        'user': request.user
    }
    return render(request, 'profile.html', context)


def editBid(request):
    put = QueryDict(request.body)
    item_id = put.get('item-id')
    item = Item.objects.get(id=item_id)
    newPrice = put.get('item-price')
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

class put1(ListView):
    model = Item
    template_name = 'put1.html'

class put2(ListView):
    model = Item
    template_name = 'put2.html'

def put3(request, pk):
    if request.method == 'PUT':
        obj = Item.objects.get(pk=pk)
        newPrice = float(QueryDict(request.body).get('price'))
        if newPrice > obj.price:
            obj.price = newPrice
            obj.save()
        else:
            error = 'Bid is lower than current price'
        obj.save()
        return JsonResponse({
            'id': obj.id,
            'price': obj.price,
            'error': error
        })
    return HttpResponse("Not a put request")

# def editBid(request, pk):
#     if request.method != 'PUT':
#         obj = Post.objects.get(pk=pk)
#         obj.price = request.POST.get('item-price')
#         obj.save()
#         return HttpResponse("Post with pk %s updated" % pk, content_type='application/json')
#     return HttpResponse("Not a put request")
