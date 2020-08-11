from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .HtmlScraper import HtmlScraper

def gameTimeView(request,title):
    json = {}
    res = HtmlScraper().search(title)
    if len(res) == 0:
        json['error'] = 'Title doesn\'t exist'
        return JsonResponse(json,status=500)
    json['results'] = 'Success'
    for item in res:
        info = {}
        info['completionist'] = item.gameplayCompletionist
        info['main'] = item.gameplayMain
        info['main+extra'] = item.gameplayMainExtra
        json[item.gameName] = info
    return JsonResponse(json)