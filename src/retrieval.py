from cachetools import cached, TTLCache
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

report_cache = TTLCache(maxsize=100, ttl=3600) 
url_cache = TTLCache(maxsize=100, ttl=3600) 

@cached(cache=url_cache)
def urlfinder(search_term):
    '''Find google search results'''
    results = 5

    page = requests.get(f"http://www.google.com/search?q={search_term}&num={results}")
    while(page.status_code == 429):
        time.sleep(5)
        page = requests.get(f"http://www.google.com/search?q={search_term}&num={results}")
        if(page.status_code ==200):
            break

    soup1 = BeautifulSoup(page.content, "html5lib")
    links = soup1.findAll("a")
    for link in links :
        link_href = link.get('href')
        if "url?q=" in link_href and not "webcache" in link_href:
            link_g = link.get('href').split("?q=")[1].split("&sa=U")[0]
            return link_g
        
@cached(cache=report_cache)
def retinfo(url) -> pd.DataFrame:
    '''Extract tables from a url'''
    new_url = url.replace("https", "http")
    url = requests.get(new_url)
    dfs = pd.read_html(url.text)
    df = dfs[0]
    return df

dfse = pd.readcsv("https://raw.githubusercontent.com/05kashyap/moneycontrol_financial-extractor/main/Equities.csv",index_col = False)
dictbse = dfse.set_index('Security Code')['Issuer Name'].to_dict()
dictnse = dfse.set_index('Security Id')['Issuer Name'].to_dict()

def __comp_name(ticker):
    if ticker.isnumeric() and len(ticker) == 6:
        ticker = int(ticker)
        return dictbse[ticker]
    elif ticker.isupper():
        return dictnse[ticker]        
    else:
        return ticker
