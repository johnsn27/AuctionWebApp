from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import SiteUsers

def start(request):
    users = SiteUsers.objects.order_by('-id')[:5]
    context = {
        'posts': users,
    }
    return render(request, 'start.html', context)

def getUser(request):
    users = SiteUsers.objects.order_by('-id')[:5]
    context = {
        'users': users,
    }
    return render(request, 'get_users.html', context)


def createUser(request):
    posts = SiteUsers.objects.all()
    response_data = {}
    if request.POST.get('action') == 'post':
        email = request.POST.get('email')
        dateOfBirth = request.POST.get('dateOfBirth')
        password = request.POST.get('password')
        response_data['email'] = email
        response_data['dateOfBirth'] = dateOfBirth
        response_data['password'] = password
        SiteUsers.objects.create(
            email=email,
            dateOfBirth=dateOfBirth,
            password=password
        )
        return JsonResponse(response_data)
    return render(request, 'create_user.html', {'posts': posts})
