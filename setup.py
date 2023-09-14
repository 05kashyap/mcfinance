from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


VERSION = "0.0.1"
DESCRIPTION = "money control financial data extractor. Requires python 3.7+"
LONG_DESCRIPTION = "First release of mcfinance"

setup(name="moneycontrol-financial_extractor",
      version=VERSION,
      author="05kashyap-ragha1992",
      author_email="<aryankashyapnaveen@gmail.com>",
      description=DESCRIPTION,
      long_description_content_type = "text/markdown",
      long_description= LONG_DESCRIPTION,
      packages=find_packages(),
      package_data={'': ['*.json']}
      install_requires = ['pandas', 'bs4', 'html5lib', 'lxml','matplotlib','requests'],
      keywords=['python','financial','extractor','data'],
      classifiers=["Developement Status :: 1 - Planning",
                   "Intended Audience :: Developers",
                   "Programming Language :: Python :: 3",
                   "Operating System :: Microsoft :: Windows",
                   ]
      )