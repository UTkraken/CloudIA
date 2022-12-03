import json
import os

from django.shortcuts import render

from cloudIA import settings


def home(request):
    f = open(os.path.join(settings.BASE_DIR, 'front\static\info.json'))
    context = dict(json.load(f))
    return render(request, "home.html", context)


def login(request):
    context = {}
    return render(request, 'template', context)


def register(request):
    context = {}
    return render(request, 'template', context)


def wishlist(request):
    context = {}
    # les métier liké
    return render(request, 'template', context)


def match(request):
    context = {}
    # retour algo
    # liste des métiers + infos
    # listes des formations correspondantes
    return render(request, 'template', context)

def onboarding_main(request):
    context = {}
    return render(request, 'template', context)

def api_onboarding(request):
    context = {}
    # une route pour l'api des info
    return render(request, 'template', context)


