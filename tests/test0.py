import unittest
import pandas as pd
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src/mcfinance')))
from helper import Extractor as ex

class Tests(unittest.TestCase):
    def test1(self):
        cmp = ex(532540, years = 13, docs = ["balance sheet"])
        #cmp.set_inputs(years = 5)
        print(cmp.get_inputs())
        cmp.get_info()
if __name__ == '__main__':
    unittest.main()
        