import pandas as pd

def create_dataframe(dict_list): #this should just be the output of the parser, lets remove it later
    return pd.DataFrame(dict_list)

def update_database(df1, df2):
    df3 = pd.concat([df1,df2])
    df3.drop_duplicates(subset=['id'], inplace=True, keep='last')
    return(df3)

def create_html(df): #going to add some arguments to get decent output
    return df.to_html('filename.html')