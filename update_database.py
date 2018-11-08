import pandas as pd

def create_dataframe(dict_list): #this takes the output of the parser
    df = pd.DataFrame(dict_list)
    cols = ['title', 'author_list', 'published', 'arxiv_primary_category', 'id', 'link']
    df = df[cols] #reorder columns
    df.sort_values(by=['published'], ascending=False) #sorts by date
    return pd.DataFrame(dict_list)

def update_database(df1, df2):
    df3 = pd.concat([df1,df2])
    df3.drop_duplicates(subset=['id'], inplace=True, keep='last') #horribly inefficient
    return(df3)

def create_html(df): #add some arguments to get decent output
    return df.to_html('filename.html')