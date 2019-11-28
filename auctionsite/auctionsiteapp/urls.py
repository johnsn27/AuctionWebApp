from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'auctionsiteapp'
urlpatterns = [
    path('', views.start, name="start"),
    path('buy', views.BuyView.as_view(), name="buy"),
    path('expired', views.ExpiredView.as_view(), name="expired"),
    path('sell', views.SellView.as_view(), name="sell"),
    path('createuser', views.createUser, name="createuser"),
    path('signup', views.signup, name="signup"),
    path('getitems', views.HomePageView.as_view(), name="getitems"),
    path('buy', views.BuyView.as_view(), name="buy"),
    path('items', views.items_json, name='itemsjson'),
    path('profile', views.viewProfile, name='profile'),
    path('editBid', views.editBid, name="editBid"),
    path('changeusername', views.changeUsername, name="changeUsername")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
