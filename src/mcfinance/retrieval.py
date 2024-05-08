from cachetools import cached, TTLCache
from bs4 import BeautifulSoup
from io import StringIO
import requests
import time
import pandas as pd
import json
import importlib.resources

url_cache = TTLCache(maxsize=100, ttl=3600) 

def pr_request(url, proxies):
    for proxy in proxies:
        try:
            page = requests.get(
            url, proxies={"http": proxy, "https": proxy})
    
            # Prints Proxy server IP address if proxy is alive.
            print("Status OK, Output:", page.text)
    
        except OSError as e:
            # Proxy returns Connection error
            print(e)    

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
        if "moneycontrol.com" in link_href and "url?q=" in link_href and not "webcache" in link_href:
            link_g = link.get('href').split("?q=")[1].split("&sa=U")[0]
            return link_g
        
def retinfo(url) -> pd.DataFrame:
    '''Extract tables from a url'''
    new_url = url.replace("https", "http")
    url = requests.get(new_url)
    dfs = None
    
    try:
        html_string = StringIO(url.text)
        dfs = pd.read_html(html_string)
    
    except(ValueError):
        return pd.DataFrame()
    
    df = dfs[0]
    return df

def comp_name(ticker):
   
    if isinstance(ticker, int):
        ticker = str(ticker)
    if ticker.isnumeric() and len(ticker) == 6:
        with importlib.resources.open_text("mcfinance.data", "dictbse.json") as f:
            dictbse = json.load(f)
        return dictbse[ticker]
    elif ticker.isupper() and ' ' not in ticker:
        with importlib.resources.open_text("mcfinance.data", "dictnse.json") as f:
            dictnse = json.load(f)
        return dictnse[ticker]        
    else:
        return ticker