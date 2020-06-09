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
        print(data)
        req = Request('{}/{}'.format(self.BASE_URL,self.SEARCH_SUFFIX),headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req,data=data) as f:
            resp = f.read().decode('utf-8')
            return resp
        return None

def test():
    htmlScraper = HtmlScraper()
    res = htmlScraper.getSearchResult(name='Halo')
    f_write = open('output.html','w')
    f_write.write(res)
    soup = bs(res) 
    prettyHTML = soup.prettify()
    print(prettyHTML)
    

test()