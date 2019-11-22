from django.urls import path

from . import views

app_name = 'auctionsiteapp'
urlpatterns = [
    path('createuser', views.createUser, name="createuser"),
    path('getuser', views.getUser, name="getuser"),
    path('', views.start, name="start"),
]
