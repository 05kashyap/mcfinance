import unittest
import pandas as pd
import os
import sys
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src/mcfinance')))
from helper import Extractor as ex

class Tests(unittest.TestCase):
    def test2(self):
            
        cmp = ex("TCS", years = 10, docs = ["ratios"])
        cmp2 = ex("Infosys", years = 10, docs = ["ratios"])
        print(cmp) 
        #cmp.plotter("Fixed Assets")
        ex.cmp_plot(comp = [cmp, cmp2], attributes = "EV/EBITDA (X)")
if __name__ == '__main__':
    unittest.main()
        