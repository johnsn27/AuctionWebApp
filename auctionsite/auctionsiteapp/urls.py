from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'auctionsiteapp'
urlpatterns = [
    path('', views.start, name="start"),
    path('createuser', views.createUser, name="createuser"),
    path('getuser', views.getUser, name="getuser"),
    path('signup', views.signup, name="signup"),
    path('getitems', views.HomePageView.as_view(), name="getitems"),
    path('auction', views.AuctionView.as_view(), name="auction"),
    path('editBid', views.editBid, name="editBid"),
    path('postitem', views.CreatePostView.as_view(), name="postitem"),
    path('search', views.SearchView.as_view(), name="search"),
    path('expiredlistings', views.ExpiredView.as_view(), name="expired"),
    path('items', views.items_json, name='itemsjson'),
    path('profile', views.viewProfile, name='profile'),
    path('listings', views.viewListings, name="listings"),
    path('put1', views.put1.as_view(), name="put1"),
    path('put2/<int:pk>', views.put2.as_view(), name="put2"),
    path('put3/<int:pk>', views.editBid, name="put3"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
