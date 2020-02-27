from django.shortcuts import render, redirect
from datetime import datetime
from .models import Datas

# Create your views here.


def index(request):

    # Sélectionne toutes les colonnes du dernier ID enregistré
    curr_day = Datas.objects.raw("SELECT * FROM wbsite_datas WHERE id=(SELECT max(id) FROM wbsite_datas)")
    for datas in curr_day:
        day = datas.day

    return render(request, 'wbsite/index.html', locals())


def graph(request):

    # Récupère les données des 7 derniers jours
    datas_week = Datas.objects.raw("SELECT * from wbsite_datas order by id desc limit 7")[::-1]

    # Récupère les données des 30 derniers jours
    datas_month = Datas.objects.raw("SELECT * from wbsite_datas order by id desc limit 30")[::-1]

    return render(request, "wbsite/graph.html", locals())


def d_day(request, day):

    # Sélectionne toutes les colonnes correspondant au nouveau jour en cours
    curr_day = Datas.objects.raw("SELECT * FROM wbsite_datas WHERE day = %s", (day,))

    # Sélectionne le dernier jour enregisté en BD
    last_day = Datas.objects.raw("SELECT * FROM wbsite_datas WHERE id=(SELECT max(id) FROM wbsite_datas)")

    # Sélectionne le premier jour enregistré en BD
    first_day = Datas.objects.raw("SELECT * FROM wbsite_datas WHERE id=(SELECT min(id) FROM wbsite_datas)")

    for datas in first_day:
        first_day = datas.day

    for datas in last_day:
        last_day = datas.day

    return render(request, 'wbsite/index.html', locals())


def contact(request):

    return render(request, "wbsite/contact.html")

