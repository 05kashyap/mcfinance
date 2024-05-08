import matplotlib.pyplot as plt
import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from mcfinance import extractors
from mcfinance import writer
from mcfinance import retrieval

class Extractor:

    def __init__(self, user_input, years = 5, docs = ["balance sheet","profit loss","cash flow"], filepath = "", proxies = "") -> None:
        '''Initialize extractor with company name, number of years and required documents'''
        try:
            self.company = retrieval.comp_name(user_input)
            self.company = self.company.replace(" ","")
        except KeyError as e:
            raise Exception("Error: Invalid ticker".format(e)) from None
        self.years = years
        self.docs = [doc.replace(" ","") for doc in docs]
        self.filepath = filepath
        self.proxies = proxies

    def __str__(self) -> str:
        return f'Extractor object, name is {self.company}, number of years is {self.years}, documents are {self.docs}'
    
    #setter method
    def set_inputs(self, user_input = None, years = None, docs = None, filepath = None) -> None:
        '''Setter method for changing/adding fields'''
        if not(user_input is None):
            self.company = retrieval.comp_name(user_input)
        if not(years is None):
            self.years = years
        if not(docs is None):
            self.docs = docs
        if not(filepath is None):
            self.filepath = docs
        return

    def get_inputs(self)-> None:
        '''Getter method to display stored info'''
        return (self.company, self.years, self.docs, self.filepath)

    

    def get_info(self, option = 1):
        '''option 0: return a dataframe; option 1: write contents to excel file'''
        
        strg = []
        for doc in self.docs:
        #generate data from docs
            stx = self.company + " moneycontrol consolidated " + doc
            if(option == 1):
                writer.excel_writer(extractors.search_gen(stx, self.years), stx.split(), filepath=self.filepath)
            else:
                df1 = writer.df_writer(extractors.search_gen(search_term=stx, period=self.years))
                strg.append(df1)
        if(option!=1):
            if len(strg) == 1: return strg[0]
            return strg
        else:
            return
       
            

    #just works dont TOUCH
    def plotter(self,*attributes):
        '''(experimental) Plots a specific company attribute over selected years'''
        attr = list(attributes)
        if len(self.docs) >1:# add cond for otherwise if user wishes to change it latr
            adict = dict(zip(attr, self.docs))
            for at, doc in adict.items():
                psearch = self.company + " moneycontrol consolidated " + doc
                X, Y = extractors.plo(attribute= at, search_term= psearch, period= self.years)
                plt.plot(X,Y,"-o", label = self.company)
                plt.xlabel("month-year")
                plt.ylabel(at)
        else:
            
            psearch = self.company + " moneycontrol consolidated " + self.docs[0]
            print(psearch)
            x = 1
            for at in attr:
                print(f"Attributes: {at}")
                plt.subplot(len(attr), 1, x)
                X, Y = extractors.plo(attribute= at, search_term= psearch, period=self.years)
                print(X)
                print(Y)
                plt.plot(X,Y,"-o", label = at)
                plt.title(self.company +" " +at + " plot")
                plt.xlabel("month-year")
                plt.ylabel(at)
                x +=1        
        plt.tight_layout()
        plt.show()
    
        

    @staticmethod
    def cmp_plot(comp, attributes):
        for company in comp:
            company.plotter(attributes)
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
        plt.tight_layout()
        plt.show()

