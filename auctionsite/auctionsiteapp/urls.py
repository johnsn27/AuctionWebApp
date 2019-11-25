from django.urls import path

from . import views

app_name = 'auctionsiteapp'
urlpatterns = [
    path('createuser', views.createUser, name="createuser"),
    path('getuser', views.getUser, name="getuser"),
    path('listings', views.viewListings, name="listings"),
    path('signup', views.signup, name="signup"),
    path('postitem/', views.CreatePostView.as_view(), name="postitem"),
    path('', views.start, name="start"),
]
