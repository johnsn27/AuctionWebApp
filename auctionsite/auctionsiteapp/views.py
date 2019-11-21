from django.http import JsonResponse
from django.shortcuts import render
from chocoapp.models import Chocolate, Flavour
from django.http import QueryDict

def login(request):
    posts = Journalist.objects.all()
    response_data = {}
    if request.POST.get(‘action’) == ‘post’:
        first_name = request.POST.get(‘first_name’)
        last_name = request.POST.get(‘last_name’)
        email = request.POST.get(‘email’)
        response_data[‘first_name’] = first_name
        response_data[‘last_name’] = last_name
        response_data[‘email’] = email
        Journalist.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        return JsonResponse(response_data)
    return render(request, ‘create_journalist.html’, {‘posts’: posts})
    })
