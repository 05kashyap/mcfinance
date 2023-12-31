import pandas as pd
import mcfinance.retrieval

def prd(url, period, last, trm, a) -> pd.DataFrame:
    '''Retrieve data for multiple years'''
    if period > a or period//5 == trm:
        df = mcfinance.retrieval.retinfo(url)
        df.drop(df.columns[[0,len(df.columns)-1]], inplace = True, axis=1)
        if(period == a+5 and last == 0):
            return df
        else:
            df.drop(columns = df.columns[-last:], inplace = True, axis=1)
        return df

def search_gen(search_term, period) -> pd.DataFrame:
    '''Handles retrieval of data and generation of urls'''
    term = period%5
    last = 5 - period
    #generate datafrane from the search term
    url = mcfinance.retrieval.urlfinder(search_term)
    urls = []
    urls = []
    for i in range(2,5):
        urlt = url + "/" + str(i) + "#" + url.split('/')[6]
        urls.append(urlt)
    #cleaning up the tables
    df1 = mcfinance.retrieval.retinfo(url)
    df1.drop(df1.columns[len(df1.columns)-1], inplace = True, axis = 1)
    if(period == 5 and last == 0):
        fdf = df1
        return fdf
    elif period < 5:
        df1.drop(columns = df1.columns[-last:], inplace = True, axis=1)
    fdf = df1
    i=1
    a = 5
    for url in urls:
        df = prd(url, period, last, i, a)
        fdf = pd.concat([fdf, df], join="inner", ignore_index=True, axis=1)
        i+=1
        a+=5
    
    fdf = fdf.drop(fdf.iloc[:, period+1:],axis = 1)
    
    return fdf

def plo(attribute, search_term, period):
    print("plotting...")
    df = search_gen(search_term, period)
    col_names = df.loc[0, :].values.flatten().tolist()
    X = col_names[1:]
    X.reverse()
    if(df[df.columns[0]] == attribute).any():
        rows = df.loc[df[df.columns[0]] == attribute].squeeze().tolist()
    else:
        raise Exception("attribute does not exist in this file")
        return
    Y = rows[1:]
    Y.reverse()
    Y = [float(i) for i in Y]
    return X,Y