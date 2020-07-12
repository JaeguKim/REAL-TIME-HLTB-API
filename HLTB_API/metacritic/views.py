from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from metacritic.MetaCriticScraper import MetaCriticScraper

def metacriticView(request,platform,title):
    baseURL = 'https://www.metacritic.com/game'
    url = '{}/{}/{}'.format(baseURL,platform,title)
    print(url)
    metacritic = MetaCriticScraper(url)
    json = metacritic.game
    return JsonResponse(json)
    # json = {}
    # for item in res:
    #     info = {}
    #     info['completionist'] = item.gameplayCompletionist
    #     info['main'] = item.gameplayMain
    #     info['main+extra'] = item.gameplayMainExtra
    #     json[item.gameName] = info
    # return JsonResponse(json)