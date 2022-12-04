import json
import os
import random

from django.shortcuts import render
from .glob import process_string
from.loss import selector

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
    print(request.GET)
    print(request.GET.getlist("interest[]"))

    # Fonction avec les paramètres
    final = selector(request.GET.getlist("interest[]"), request.GET['caractere'], request.GET['working_place'], request.GET['filiere'])
    # final = selector('aventure', 'sportif', 'port', 'marchand')
    # ouverture du json
    data = open(os.path.join(settings.BASE_DIR, 'front\static\hand.json'))
    data = json.load(data)

    final_total = 0
    for it in list(final.keys()):
        final_total = final_total + final[it]

    for d in data:
        print(d['keyword'])
        print(final)
        score = 0
        for kw in d['keyword']:
            score = score + final[kw]
        print(score)
        d["score"] = (score / final_total) * 5
        d["keyword"] = "\",\"".join(d["keyword"])
        d["secteurs"] = "\",\"".join(d["secteurs"])
        for key in list(d.keys()):
            if type(d[key]) == str:
                d[key] = process_string(d[key])
    # une route pour l'api des info
    context = {}
    context["jobs"] = data
    context["jobs"] = sorted(data, key=lambda d: d['score'])
    context["dump"] = json.dumps(context["jobs"], indent=4, separators=(',', ': '), sort_keys=True)
    return render(request, 'api.html', context)


def thanks(request):
    context = {}
    # une route pour l'api des info
    return render(request, 'thanks.html', context)


