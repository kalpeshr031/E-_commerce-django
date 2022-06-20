from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="ReadShop"),
    path('about/', views.index, name="aboutUs"),
    path('contact', views.contact, name="contactUs"),
    path('tracker', views.tracker, name="trackingStatus"),
    path('search', views.search, name="search"),
    path('productView', views.productView, name="product"),
    path('checkout', views.checkout, name="checkout"),
]

