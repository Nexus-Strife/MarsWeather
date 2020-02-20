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


def re_dir_prev(request, day):  # Méthode de redirection d'url pour le jour précédent

    # Sélectionne l'ID du jour en cours pour le décrémenter de 1 afin de passer au jour précédent
    coming_from = Datas.objects.raw("SELECT id FROM wbsite_datas WHERE day = %s", (day, ))

    for id in coming_from:
        new_id = id.id
        new_id -= 1

    # Sélectionne le jour précédent après avoir décrémenter l'ID du jour en cours
    curr_day = Datas.objects.raw("SELECT * FROM wbsite_datas WHERE id = %s", (new_id, ))
    for datas in curr_day:
        day = datas.day

    # Redirige vers la vue qui avec la bonne url
    return redirect(prev_day, day=day)


def re_dir_next(request, day):  # Méthode de redirection d'url pour le jour suivant

    # Sélectionne l'ID du jour en cours pour le décrémenter de 1 afin de passer au jour précédent
    coming_from = Datas.objects.raw("SELECT id FROM wbsite_datas WHERE day = %s", (day, ))

    for id in coming_from:
        new_id = id.id
        new_id += 1

    # Sélectionne le jour précédent après avoir décrémenter l'ID du jour en cours
    curr_day = Datas.objects.raw("SELECT * FROM wbsite_datas WHERE id = %s", (new_id, ))
    for datas in curr_day:
        day = datas.day

    # Redirige vers la vue qui avec la bonne url
    return redirect(next_day, day=day)


def prev_day(request, day):

    # Sélectionne toutes les colonnes correspondant au nouveau jour en cours
    curr_day = Datas.objects.raw("SELECT * FROM wbsite_datas WHERE day = %s", (day, ))
    for datas in curr_day:
        day = datas.day

    return render(request, 'wbsite/index.html', locals())


def next_day(request, day):

    # Sélectionne toutes les colonnes correspondant au nouveau jour en cours
    curr_day = Datas.objects.raw("SELECT * FROM wbsite_datas WHERE day = %s", (day, ))
    for datas in curr_day:
        day = datas.day

    return render(request, 'wbsite/index.html', locals())


def test(request):
    x_data = [416, 426, 429, 430, 431]
    y_data = [-68, -66, -59, -61, -59]
    y_prime = [-15, -9, -10, -13, -12]
    y_beta = [-94, -92, -95, -93, -94]

    return render(request, 'wbsite/test.html', locals())

