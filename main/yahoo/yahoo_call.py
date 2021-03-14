from bs4 import BeautifulSoup as bs4
import requests

class YahooCall:

    def call(self, market='GOLD'):
        """
        market is SILVER for silver and anthing else for gold
        """
        market = 'SI' if market == 'SILVER' else 'GC'

        r = requests.get(f"https://finance.yahoo.com/quote/{market}=F?p=GC=F&.tsrc=fin-srch").content

        soup = bs4(r, 'html.parser')
            

        titles = soup.find_all('h3')
        links = []
        for title in titles[3:]:
            link = title.find('a')
            links.append(link.get('href'))

        articles = []
        for link in links:
            r = requests.get(f"https://finance.yahoo.com{link}").content
            soup = bs4(r, 'html.parser')

            body = soup.find('div', attrs={'class': 'caas-body'}).get_text()
            articles.append(body)

        return articles


