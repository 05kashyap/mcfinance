import extractor as ex

TCS = ex.FinancialExtractor("TCS",10)
TCS.get_info()
TCS.plotter(attr='Tangible Assets')