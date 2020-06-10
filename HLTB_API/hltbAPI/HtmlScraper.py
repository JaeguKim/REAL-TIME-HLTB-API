from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
from urllib import parse

class HtmlScraper:
    BASE_URL = 'https://howlongtobeat.com'
    SEARCH_SUFFIX = 'search_results.php'

    def getSearchResult(self,name):
        body = {
            'queryString': name,
            't': 'games',
            'sorthead': 'popular',
            'sortd': 'Normal Order',
            'plat': '',
            'length_type': 'main',
            'length_min': '',
            'length_max': '',
            'detail': '0'
        }
        data = parse.urlencode(body).encode("utf-8")
        req = Request('{}/{}'.format(self.BASE_URL,self.SEARCH_SUFFIX),headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req,data=data) as f:
            resp = f.read().decode('utf-8')
            return resp
        return None

def parseHTML(soup):
    if len(soup.h3) > 0:
        liElements = soup.findAll('li')
        for elem in liElements:
            gameTitleAnchor = elem.findAll('a')[0]
            gameName = gameTitleAnchor.get('title')
            detailId = gameTitleAnchor.get('href')[gameTitleAnchor.get('href').index('?id=')+4:]
            print(gameName)
            print(detailId)
            gameImage = gameTitleAnchor.findAll('img')[0].get('src')
            print(gameImage)
            timeLabels = []
            main = 0; mainExtra = 0; complete = 0
            soup.select("div[class*=span3]")
            for gameTimeInfo in  elem.select("div[class*=search_list_tidbit]"):
                print(gameTimeInfo)

def test():
    htmlScraper = HtmlScraper()
    res = htmlScraper.getSearchResult(name='Halo')
    f_write = open('output.html','w')
    f_write.write(res)
    soup = bs(res,features="html.parser")
    parseHTML(soup)
    #prettyHTML = soup.prettify()
    #print(prettyHTML)
    

test()