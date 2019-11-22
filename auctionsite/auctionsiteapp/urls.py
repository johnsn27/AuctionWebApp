from django.urls import path

from . import views

app_name = 'auctionsiteapp'
urlpatterns = [
    path('createuser', views.login, name="createuser"),
]
