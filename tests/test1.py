import unittest
import pandas as pd
import os
import sys
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'mcfinance'))
from helper import Extractor as ex

class Tests(unittest.TestCase):
    def test1(self):

        cmp = ex(532540, years = 10, docs = ["ratios"])
        data = cmp.get_info(0)
        print(data)
        self.assertIsInstance(data, list)
if __name__ == '__main__':
    unittest.main()
        