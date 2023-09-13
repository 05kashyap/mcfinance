import matplotlib.pyplot as plt

import extractors
import writer
import retrieval

class Extractor:

    def __init__(self, user_input, years = 10, docs = ["balance sheet","profit loss","cash flow"], filepath = "") -> None:
        '''Initialize extractor with company name, number of years and required documents'''
        self.company = retrieval.comp_name(user_input)
        self.company = self.company.replace(" ","")
        self.years = years
        self.docs = [doc.replace(" ","") for doc in docs]
        self.filepath = filepath
    
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
        print("retrieving data...")
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
            return strg
        else:
            return
    #just works dont TOUCH
    def plotter(self,*attributes):
        '''(experimental) Plots a specific company attribute over selected years'''
        attr = list(attributes)
        adict = dict(zip(attr, self.docs))
        for at, doc in adict.items():
            psearch = self.company + " moneycontrol consolidated " + doc
            X, Y = extractors.plo(attribute= at, search_term= psearch, period= self.years)
            plt.plot(X,Y,"-o", label = self.company)
            plt.xlabel("month-year")
            plt.ylabel(at)
            
            #plt.show()

    @staticmethod
    def cmp_plot(comp, attributes):
        for company in comp:
            company.plotter(attributes)
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
        plt.tight_layout()
        plt.show()

