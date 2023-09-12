import matplotlib.pyplot as plt

class Extractor:
    import retrieval
    def __init__(self, user_input, years = 10, docs = ["balance sheet","profit loss","cash flow"], filepath = "") -> None:
        '''Initialize extractor with company name, number of years and required documents'''
        self.company = self.retrieval.comp_name(user_input)
        self.company = self.company.replace(" ","")
        self.years = years
        self.docs = [doc.replace(" ","") for doc in docs]
        self.filepath = filepath
        

    import extractors
    import writer

    def get_info(self, option = 1):
        '''option 0: return a dataframe; option 1: write contents to excel file'''
        print("retrieving data...")
        strg = []
        for doc in self.docs:
        #generate data from docs
            stx = self.company + " moneycontrol consolidated " + doc
            if(option == 1):
                self.writer.excel_writer(self.extractors.search_gen(stx, self.years), stx.split(), filepath=self.filepath)
            else:
                df1 = self.writer.df_writer(self.extractors.search_gen(search_term=stx, period=self.years))
                strg.append(df1)
        if(option!=1):
            return strg
        else:
            return
    #just works dont TOUCH
    def plotter(self,attribute):
        '''(experimental) Plots a specific company attribute over selected years'''
        X, Y = self.extractors.plo(attribute= attribute, search_term=self.company + " moneycontrol consolidated " + self.docs[0], period= self.years)
        plt.plot(X,Y,"-o")
        plt.xlabel("month-year")
        plt.ylabel(attribute)
        plt.show()

    def ratios(self):
        pass
