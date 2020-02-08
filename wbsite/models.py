from django.db import models

# Create your models here.


class Datas(models.Model):
    day = models.IntegerField()
    mx_temp = models.IntegerField()
    mn_temp = models.IntegerField()
    avg_temp = models.IntegerField()
    season = models.CharField(max_length=9)
    avg_dir_wind = models.CharField(max_length=5)
    current_month_text = models.CharField(max_length=10)
    current_year_short = models.IntegerField()

