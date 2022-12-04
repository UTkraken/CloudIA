import json
import os
import random

from django.shortcuts import render
from .glob import process_string

from cloudIA import settings


def home(request):
    f = open(os.path.join(settings.BASE_DIR, 'front\static\info.json'))
    context = dict(json.load(f))
    return render(request, "home.html", context)


def login(request):
    context = {}
    return render(request, 'login.html', context)


def register(request):
    context = {}
    return render(request, 'register.html', context)


def wishlist(request):
    #métiers liké
    f = open(os.path.join(settings.BASE_DIR, 'front\static\hand.json'))
    context = {}
    ls_job = json.load(f)
    random.shuffle(ls_job)
    for job in ls_job:
        for key in list(job.keys()):
            if type(job[key]) == str:
                job[key] = process_string(job[key])
    context["wishlist"] = ls_job[0:3]
    for wish in context["wishlist"]:
        wish["desc"] = wish["short"][0:100] + "..."
        wish["secteurs"] = ", ".join(wish["secteurs"])[0:-2]
    return render(request, 'wishlist.html', context)


def match(request):
    context = {}
    # retour algo
    # liste des métiers + infos
    # listes des formations correspondantes
    return render(request, 'result.html', context)

def onboarding_main(request):
    context = {}
    return render(request, 'onboarding.html', context)

def api_onboarding(request):
    context = {}
    # une route pour l'api des info
    return render(request, 'template', context)


def thanks(request):
    context = {}
    # une route pour l'api des info
    return render(request, 'thanks.html', context)


