from django.contrib import admin
from django.urls import path, include
from front import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('match', views.match, name='match'),
    path('onboarding', views.onboarding_main, name='onboarding'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('api/onboarding', views.api_onboarding, name='api-onboarding')
]