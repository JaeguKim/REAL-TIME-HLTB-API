from django.shortcuts import render
from rest_framework import generics
from .models import Currency
from django.http import HttpResponse,JsonResponse
from .HtmlScraper import HtmlScraper
from .serializers import CurrencySerializer
 
class ListCurrencyView(generics.ListAPIView):
    queryset = Currency.objects.all() # used for returning objects from this view
    serializer_class = CurrencySerializer

def gameTimeView(request,title):
    res = HtmlScraper().search(title)
    json = {}
    for item in res:
        info = {}
        info['completionist'] = item.gameplayCompletionist
        info['main'] = item.gameplayMain
        info['main+extra'] = item.gameplayMainExtra
        json[item.gameName] = info
    return JsonResponse(json)