from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


VERSION = "0.1.8"
DESCRIPTION = "Money control financial data extractor-Requires python 3.7+"
LONG_DESCRIPTION = long_description

setup(name="mcfinance",
      version=VERSION,
      author="05kashyap-ragha1992",
      author_email="<aryankashyapnaveen@gmail.com>",
      description=DESCRIPTION,
      long_description_content_type = "text/markdown",
      long_description= LONG_DESCRIPTION,
      packages=['mcfinance'],
      package_dir={'mcfinance': 'src/mcfinance'},
      package_data={'mcfinance': ['data/*.json']},
      install_requires = ['pandas', 'bs4', 'html5lib', 'lxml','matplotlib','requests','openpyxl','PyQt5'],
      keywords=['python','financial','extractor','data'],
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "Programming Language :: Python :: 3.11",
                   "Operating System :: Microsoft :: Windows",
                   ]
      )