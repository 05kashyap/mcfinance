import pandas as pd

def excel_writer(daf, words, filepath) -> None:
    '''Write dataframe into pandas dataframe or excel file'''
    web, name, info = words[1], words[0], words[3]
    if filepath != "":
        filepath += "/"
    writer = pd.ExcelWriter(filepath+web+'_'+name+'_'+info+'.xlsx')
    daf.to_excel(writer)
    writer.close()
    print(f'{name} {info} data is written successfully to Excel File.')
    
def df_writer(daf) -> pd.DataFrame:
    return daf