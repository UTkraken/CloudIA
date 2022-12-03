from django.contrib import admin
from django.urls import path, include
from front import views

urlpatterns = [
    path('', views.home, name='home'),
    # Onboarding
    # Wishlist
    # Coup de coeur
    # login
    # register
    # Homepage
]