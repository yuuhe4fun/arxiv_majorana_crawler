import pandas as pd

def create_dataframe(dict_list): #this takes the output of the parser, but probably should just be the output of the parser
    df = pd.DataFrame(dict_list)
    return df

def update_database(df1, df2):
    df3 = pd.concat([df1,df2])
    df3.drop_duplicates(subset=['id'], inplace=True, keep='last') #horribly inefficient
    cols = ['title', 'author_list', 'published', 'arxiv_primary_category', 'id', 'link']
    df3 = df3[cols] #reorder columns
    df3.sort_values(by=['published'], ascending=False) #sorts by date
    return(df3)

def create_html(df): #add some arguments to get decent output, but shouldn't really be in here
    pd.set_option('display.max_rows', len(df))
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', -1)
    df.to_html('filename.html', index=False)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.max_colwidth')