"""MarsWeather URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('graph', views.graph, name='graph'),
    path('b/<day>/', views.re_dir_prev, name='re_dir_prev'),
    path('<day>/', views.prev_day, name='prev_day'),
    path('a/<day>/', views.re_dir_next, name='re_dir_next'),
    path('<day>/', views.next_day, name='next_day'),
    path('test/test/', views.test, name='test')

]
