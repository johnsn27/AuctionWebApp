from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'auctionsiteapp'
urlpatterns = [
    path('', views.start, name="start"),
    path('createuser', views.createUser, name="createuser"),
    path('getuser', views.getUser, name="getuser"),
    path('listings', views.viewListings, name="listings"),
    path('signup', views.signup, name="signup"),
    path('getitems', views.HomePageView.as_view(), name="getitems"),
    path('postitem/', views.CreatePostView.as_view(), name="postitem"),
    path('search', views.SearchView.as_view(), name="search"),
    path('expiredlistings', views.ExpiredView.as_view(), name="expired"),
    path('items', views.items_json, name='itemsjson'),
    path('profile', views.viewProfile, name='profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
