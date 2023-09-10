import unittest
import pandas as pd
import os
import sys
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from helper import Extractor as ex

class Tests(unittest.TestCase):
    def test1(self):

        cmp = ex("TCS", years = 10, docs = ["balance sheet"])
        data = cmp.get_info(0)
        self.assertIsInstance(data, pd.DataFrame, "success")
if __name__ == '__main__':
    unittest.main()
        