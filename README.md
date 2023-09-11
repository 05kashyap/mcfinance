#moneycontrol financial_extractor

Currently in experimentation phase

Developed by ragha1992 and 05kashyap

## Description:

Extract financial data from the money control website using the company name, BSE or NSE number(experimental).
Export any selected data into either pandas dataframe or excel sheet with ease!
## Usage:
### Initialise company details:
```python
import extractor as ex
Company = ex.FinancialExtractor(user_input= "Company_name")
#years and docs are default
Company = ex.FinancialExtractor(user_input= "Company_name",years = 10, docs = ["balance sheet", "profit loss"])
```

### Export company details as excel file (default)
```python
Company.get_info()
```
### Export company details into pandas data frame
```python
Company.get_info(option=1)
```

### Plot certain attribute over selected years(experimental)
```python
company.plotter(attribute = "certain file attribute of the document")
```
