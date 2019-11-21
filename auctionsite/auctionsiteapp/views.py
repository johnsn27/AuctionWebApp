from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import User


def login(request):
    posts = User.objects.all()
    response_data = {}
    if request.POST.get('action') == 'post':
        email = request.POST.get('email')
        dateOfBirth = request.POST.get('dateOfBirth')
        password = request.POST.get('password')
        response_data['email'] = email
        response_data['dateOfBirth'] = dateOfBirth
        response_data['password'] = password
        User.objects.create(
            email=email,
            dateOfBirth=dateOfBirth,
            password=password
        )
        return JsonResponse(response_data)
    return render(request, 'create_user.html', {'posts': posts})
