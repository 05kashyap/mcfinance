import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
import html5lib
import lxml
from cachetools import cached, TTLCache
import matplotlib.pyplot as plt
import time

class FinancialExtractor:
    report_cache = TTLCache(maxsize=100, ttl=3600) 
    url_cache = TTLCache(maxsize=100, ttl=3600) 
    
    def __init__(self, user_input, years = 10, docs = ["balance sheet","profit loss","cash flow"], filepath = "") -> None:
        '''Initialize extractor with company name, number of years and required documents'''
        self.user_input = user_input.replace(" ","")
        self.years = years
        self.docs = docs
        if(self.user_input.isnumeric() and len(self.user_input) == 6):
            self.company = self.__comp_name(self.user_input)
        else:
            self.company = self.user_input
        self.filepath = filepath

    def plotter(self,attr,doc="balance sheet"):
        '''(experimental) Plots a specific company attribute over selected years'''
        print("plotting...")
        df = self.search_gen(self.company+" moneycontrol consolidated "+ doc, self.years)
        row_num = df[df[df.columns[0]] == attr].index
        #column_names = list(df.columns)
        col_names = df.loc[0, :].values.flatten().tolist()
        X = col_names[1:]
        X.reverse()
        row_list = df.loc[row_num, :].values.flatten().tolist()
        Y = row_list[1:]
        Y.reverse()
        Y = [float(i) for i in Y]
        plt.plot(X,Y,"-o")
        plt.xlabel("month-year")
        plt.ylabel(attr)
        plt.show()

    @cached(cache=report_cache)
    def __urlfinder(self,search_term):
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

    def __comp_name(self, ticker):
        '''Find company name from ticker number (experimental)'''
        page = requests.get(f"https://www.google.com/search?q=bombay+india+{ticker}")
        soup1 = BeautifulSoup(page.content, "html5lib")
        links = soup1.findAll("a")
        for link in links:
            link_href = link.get('href')
            if "url?q=" in link_href and not "webcache" in link_href:
                link_g = link.get('href').split("?q=")[1].split("&sa=U")[0]
                if (link_g.split('.')[1] == "bseindia"):
                    return link_g.split("/")[4]
                
    @cached(cache=report_cache)
    def __retinfo(self, url) -> pd.DataFrame:
        '''Extract tables from a url'''
        new_url = url.replace("https", "http")
        url = requests.get(new_url)
        dfs = pd.read_html(url.text)
        df = dfs[0]
        return df

    def __excel_writer(self, daf, words) -> None:
        '''Write dataframe into .excel file'''
        web, name, info = words[1], words[0], (words[3]+words[4])
        if self.filepath != "":
            self.filepath += "/"
        writer = pd.ExcelWriter(self.filepath+web+'_'+name+'_'+info+'.xlsx')
        daf.to_excel(writer)
        writer.close()
        print(f'{name} {info} data is written successfully to Excel File.')

    def __prd(self, url, period, last, trm, a) -> pd.DataFrame:
        '''Retrieve data for multiple years'''
        if period > a or period//5 == trm:
            df = self.__retinfo(url)
            df.drop(df.columns[[0,len(df.columns)-1]], inplace = True, axis=1)
            if(period == a+5 and last == 0):
                return df
            else:
                df.drop(columns = df.columns[-last:], inplace = True, axis=1)
            return df

    def search_gen(self, search_term, period) -> pd.DataFrame:
        '''Handles retrieval of data and generation of urls'''
        term = period%5
        last = 5 - period
        #generate datafrane from the search term
        url = self.__urlfinder(search_term)
        urls = []
        urls = []
        for i in range(2,5):
            urlt = url + "/" + str(i) + "#" + url.split('/')[6]
            urls.append(urlt)
        #cleaning up the tables
        df1 = self.__retinfo(url)
        df1.drop(df1.columns[len(df1.columns)-1], inplace = True, axis = 1)
        if(period == 5 and last == 0):
            fdf = df1
            return fdf
        elif period < 5:
            df1.drop(columns = df1.columns[-last:], inplace = True, axis=1)
        fdf = df1
        i=1
        a = 5
        for url in urls:
            df = self.__prd(url, period, last, i, a)
            fdf = pd.concat([fdf, df], join="inner", ignore_index=True, axis=1)
            i+=1
            a+=5
        
        fdf = fdf.drop(fdf.iloc[:, self.years+1:],axis = 1)
        
        return fdf

    def get_info(self) -> None:
        '''User callable function to retrieve required data'''
        print("retrieving data...")
        for doc in self.docs:
        #generate data from docs
            stx = self.company
            stx += " moneycontrol consolidated "+ doc
            self.__excel_writer(self.search_gen(stx, self.years), stx.split())