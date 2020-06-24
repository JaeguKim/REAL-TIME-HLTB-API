from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .HtmlScraper import HtmlScraper

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