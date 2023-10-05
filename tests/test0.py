import unittest
import pandas as pd
import os
import sys
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'mcfinance'))
from mcfinance.helper import Extractor as ex

class Tests(unittest.TestCase):
    def test1(self):
        cmp = ex(532540, years = 10, docs = ["balance sheet", "ratios"])
        cmp.set_inputs(years = 5)
        print(cmp.get_inputs())
        cmp.get_info()
if __name__ == '__main__':
    unittest.main()
        