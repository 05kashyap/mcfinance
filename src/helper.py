import matplotlib.pyplot as plt

class Extractor:
    def __init__(self, user_input, years = 10, docs = ["balance sheet","profit loss","cash flow"], filepath = "") -> None:
        '''Initialize extractor with company name, number of years and required documents'''
        self.user_input = user_input.replace(" ","")
        self.years = years
        self.docs = [doc.replace(" ","") for doc in docs]
        if(self.user_input.isnumeric() and len(self.user_input) == 6):
            self.company = self.__comp_name(self.user_input)
        else:
            self.company = self.user_input
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
    def plotter(self,*attributes):
        '''(experimental) Plots a specific company attribute over selected years'''
        attr = list(attributes)
        adict = dict(zip(attr, self.docs))
        for at, doc in adict.items():
            psearch = self.company + " moneycontrol consolidated " + doc
            X, Y = self.extractors.plo(attribute= at, search_term= psearch, period= self.years)
            plt.plot(X,Y,"-o")
            plt.xlabel("month-year")
            plt.ylabel(at)
            plt.show()
