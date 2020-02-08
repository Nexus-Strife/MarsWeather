from django.shortcuts import render, redirect
import requests
from datetime import datetime
from .models import Datas
from plotly.offline import plot
from plotly.graph_objects import Scatter

# Create your views here.


def index(request):

    # Sélectionne toutes les colonnes du dernier ID enregistré
    curr_day = Datas.objects.raw("SELECT * FROM wbsite_datas WHERE id=(SELECT max(id) FROM wbsite_datas)")
    for datas in curr_day:
        day = datas.day

    return render(request, 'wbsite/index.html', locals())


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




