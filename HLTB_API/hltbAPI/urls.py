from django.urls import path
from . import views

app_name = 'hltbAPI'
urlpatterns = [
   path('<str:title>/',views.gameTimeView,name='result'),
]
