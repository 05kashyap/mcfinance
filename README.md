# financial_extractor

Currently in experimentation phase

Developed by ragha1992 and 05kashyap

## Description:

Extract financial data from the money control website using the company name, BSE or NSE number(experimental).
Export any selected data into either pandas dataframe or excel sheet with ease!
 
## Usage:
### Initialise company details:
#### Create an Extractor instance with company namr (required) and/or number of years(default), required documents(default), and filepath to write documents(default current directory).

```python
import extractor
Company = Extractor(user_input= "Company_name")
#years and docs are default
Company = Extractor(user_input= "Company_name",years = 10, docs = ["balance sheet", "profit loss"], filepath = "/files")
```

### Export company details as excel file (default)
#### The get_info() function can be used to extract and store company data in an excel file. The file will be stored in the current filepath or the user defined filepath as per object initialisation 

```python
Company.get_info()
or
Company.get_info(option = 1)
```

### Export company details into pandas data frame

```python
DataFrame1, DataFrame2, DataFrame3 = Company.get_info(option = 0)
```

### Plot certain attribute over selected years using matplotlib (experimental)
#### The plotter() function can be used to show the companies attribute from a certain document over the selected period of time using a line graph from the matplotlib library. The function accepts a single required arguement for the attribute selection. 

```python
company.plotter(attribute = "certain file attribute of the document")
```
