import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
import html5lib 
import lxml

class Financial_Extractor:
    
    def __init__(self, user_input, years = 10, docs = ["balance sheet","profit loss","cash flow"], filepath = "") -> None:
        self.user_input = user_input.replace(" ","")
        self.years = years
        self.docs = docs
        self.filepath = filepath

    def __urlfinder(self,search_term):
        results = 5
        page = requests.get(f"https://www.google.com/search?q={search_term}&num={results}")
        soup1 = BeautifulSoup(page.content, "html5lib")
        links = soup1.findAll("a")
        for link in links :
            link_href = link.get('href')
            if "url?q=" in link_href and not "webcache" in link_href:
                link_g = link.get('href').split("?q=")[1].split("&sa=U")[0]
                return link_g
            
    def __comp_name(self,ticker):
        page = requests.get(f"https://www.google.com/search?q=bombay+india+{ticker}")
        soup1 = BeautifulSoup(page.content, "html5lib")
        links = soup1.findAll("a")
        for link in links :
            link_href = link.get('href')
            if "url?q=" in link_href and not "webcache" in link_href:
                link_g = link.get('href').split("?q=")[1].split("&sa=U")[0]
                if(link_g.split('.')[1] == "bseindia"):
                    return link_g.split("/")[4]
        
    def __retinfo(self, url) -> pd.DataFrame:
        new_url = url.replace("https","http")
        url = requests.get(new_url)
        dfs = pd.read_html(url.text)
        df = dfs[0]
        return df

    def __excel_writer(self, daf, words,filepath) -> None:
        web, name, info = words[1], words[0], (words[3]+words[4])
        if filepath != "":
            filepath += "/"
        writer = pd.ExcelWriter(filepath+web+'_'+name+'_'+info+'.xlsx')
        daf.to_excel(writer)
        writer.close()
        print(f'{name} {info} data is written successfully to Excel File.')
    
    def __prd(self, url, period, last, trm, a) -> pd.DataFrame:
        if period > a or period//5 == trm:
            df = self.__retinfo(url)
            df.drop(df.columns[[0,6]], inplace = True, axis=1)
            if(period == a+5 and last == 0):
                return df
            else:
                df.drop(columns = df.columns[-last:], inplace = True, axis=1)
            return df

    def __search_gen(self, search_term, period) -> pd.DataFrame:
        term = period%5
        last = 5 - period
        #generate datafrane from the search term
        url = self.__urlfinder(search_term)
        url2 = url + "/2#" + url.split('/')[6]
        url3 = url + "/3#" + url.split('/')[6]
        url4 = url + "/4#" + url.split('/')[6]
        urls = [url2, url3, url4]
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
        return fdf

    def get_info(self) -> None:
        company = ""
        if(self.user_input.isnumeric() and len(self.user_input) == 6):
            company+= self.__comp_name(self.user_input)
        else:
            company+= self.user_input
        for doc in self.docs:
        #generate data from docs
            stx = company
            stx += " moneycontrol consolidated "+ doc
            self.__excel_writer(self.__search_gen(stx, self.years), stx.split(),filepath = self.filepath)
