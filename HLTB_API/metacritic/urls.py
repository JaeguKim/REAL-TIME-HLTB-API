from django.urls import path
from . import views

app_name = 'metacritic'
urlpatterns = [
   path('<str:platform>/<str:title>/',views.metacriticView,name='result'),
]