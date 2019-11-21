from django.contrib import admin
from django.urls import path
from auctionsiteapp.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createuser', login, name="createuser")
]
