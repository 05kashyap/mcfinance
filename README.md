# mcfinance

### Developed by 05kashyap and ragha1992
### PyPI stats:
[![Downloads](https://static.pepy.tech/badge/mcfinance)](https://pepy.tech/project/mcfinance)
## Description:

Extract financial data from the money control website using the company name, BSE or NSE number.
Export any selected data into either pandas dataframe or excel sheet with ease!
### .

*Disclaimer*: We are in no way affiliated with moneycontrol.com
 
## Usage:
```python
pip install mcfinance
```
### Initialise company details:
#### Create an Extractor instance with company name/ BSE/ NSE ID (required) and/or number of years(default), required documents(default), and filepath to write documents(default current directory).

```python
from mcfinance import Extractor
Company = Extractor(user_input= "Company_name")
#years and docs are default
Company = Extractor(user_input= "Company_name",years = 10, docs = ["balance sheet", "profit loss"], filepath = "/files")
```
any of the inputs can be changed later on as per user convenience
```python
Company.set_inputs(years = 6)
```
### Export company details as excel file (default)
#### The get_info() function can be used to extract and store company data in an excel file. The file will be stored in the current filepath or the user defined filepath as per object initialisation 

```python
Company.get_info()
```
or
```python
Company.get_info(option = 1)
```

### Export company details into pandas data frame

```python
DataFrame1, DataFrame2, DataFrame3 = Company.get_info(option = 0)
```
### Plot certain attribute over selected years using matplotlib
#### The plotter() function can be used to show the companies attribute from a certain document over the selected period of time using a line graph from the matplotlib library. The function accepts a single required arguement for the attribute selection. 

```python
company.plotter("certain file attribute of the document")
```
#### Usage example: 

```python
cmp = Extractor("TCS", years = 10, docs = ["ratios"])
cmp.plotter("EV/EBITDA (X)")
```
output:

![image](https://github.com/05kashyap/moneycontrol_financial-extractor/assets/120780494/f5be744e-e065-4b03-b6df-2ca7e765c4b2)

### We can also plot the data of multiple companies on the same graph for comparison purposes
```python
company1 = Extractor("TCS", years = 10, docs = ["ratios"])
company2 = Extractor("Infosys", years = 10, docs = ["ratios"])
Extractor.cmp_plot(comp = [company1, company2], attributes = "EV/EBITDA (X)")
```
output:

![image](https://github.com/05kashyap/mcfinance/assets/120780494/294f8313-2876-4751-9485-18517dccb0d3)
