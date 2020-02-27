import mysql.connector
from mysql.connector import errorcode
import requests
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from wbsite.models import Datas

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'password',
    'port': '3307',
    'database': 'Mars_weather'
}


class Command(BaseCommand):
    help = "Update once per day the information in the DB"

    def handle(self, *args, **options):

        r = requests.get('https://api.nasa.gov/insight_weather/?api_key=clé&feedtype=json&ver=1.0')
        meteo = r.json()

        # Connection à la BD
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(buffered=True)

        # Essaie de créer la table si elle n'existe pas
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS wbsite_datas(id INT AUTO_INCREMENT PRIMARY KEY, "
                           "day INT, mx_temp INT, min_temp INT, avg_temp INT, current_month_text VARCHAR(10), "
                           "current_year_short INT, season VARCHAR(9), avg_dir_wind VARCHAR(5))")
        except mysql.connector.Error as err:
            print(err)
            exit(1)

        # Jour en cours, le 7ème
        curr_day = meteo["sol_keys"][6]

        # Température max, min et moyenne
        mx_temp = round(meteo[curr_day]["AT"]["mx"])
        min_temp = round(meteo[curr_day]["AT"]["mn"])
        avg_temp = round(meteo[curr_day]["AT"]["av"])

        # Jour, mois et année terrienne en cours
        current_month_text = datetime.now().strftime('%B')
        current_year_short = datetime.now().strftime('%Y')
        current_earth_day = datetime.now().strftime('%d') - 1

        # Saison en cours
        season = meteo[curr_day]["Season"]
        if season == "summer":
            season = "Été"
        elif season == "autumn":
            season = "Automne"
        elif season == "spring":
            season = "Printemps"
        elif season == "winter":
            season = "Hiver"

        # Direction moyenne des vents pour le jour en cours
        avg_dir_wind = meteo[curr_day]["WD"]["most_common"]["compass_point"]

        cursor.execute("INSERT INTO wbsite_datas(day, mx_temp, min_temp, avg_temp, current_earth_day, current_month_text,"
                       " current_year_short, season, avg_dir_wind) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (curr_day, mx_temp, min_temp, avg_temp, current_earth_day, current_month_text,
                        current_year_short, season, avg_dir_wind))
        cnx.commit()
