import unittest
import pandas as pd
import os
import sys
import sys, os  
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src/mcfinance')))
from helper import Extractor as ex

class Tests(unittest.TestCase):
    def test1(self):

        cmp = ex("TCS", years=10, docs = ["balance sheet"])
        cmp.get_info(1)
        #print(df1.head())
        #self.assertIsInstance(df1, pd.DataFrame)
if __name__ == '__main__':
    unittest.main()
        