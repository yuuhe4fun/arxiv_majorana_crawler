import pandas as pd
import bs4
from datetime import datetime

def create_dataframe(dict_list): #this takes the output of the parser, but probably should just be the output of the parser
    df = pd.DataFrame(dict_list)
    return df

def update_database(df1, df2):
    df3 = pd.concat([df1,df2])
    df3.drop_duplicates(subset=['id'], inplace=True, keep='last') #could be done more efficiently?
    cols = ['title', 'author_list', 'published', 'arxiv_primary_category', 'id', 'link']
    df3 = df3[cols] #reorder columns
    # df3['title'] = df3['title'].apply(_remove_newlines) #take out new lines
    # df3['published'] = df3['published'].apply(_convert_time) #convert time to something legible, could go into parser
    df3.sort_values(by=['published'], ascending=False) #sorts by date
    return(df3)

def create_html(df, filename): #add some arguments to get decent output, but shouldn't really be in here
    pd.set_option('display.max_rows', len(df))
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', -1)
    df['link'] = df['link'].apply(_make_clickable) #make hyperlinks clickable
    #df['author_list'] = df['author_list'].apply(_make_utf8) #set correct encoding for html
    df.to_html(filename, escape=False, index=False, justify='left')
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.max_colwidth')
    
    with open(filename) as inf:
        txt = inf.read()
    soup = bs4.BeautifulSoup(txt)
    metatag = soup.new_tag('meta')
    metatag.attrs['http-equiv'] = 'Content-Type'
    metatag.attrs['content'] = 'text/html; charset=utf-8'
    soup.head.append(metatag)
    mathjaxtag2 = soup.new_tag('script')
    mathjaxtag2.attrs['type'] = 'text/javascript' 
    mathjaxtag2.attrs['src'] = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS-MML_HTMLorMML' 
    soup.head.insert(1, mathjaxtag2)
    mathjaxtag1 = soup.new_tag('script')
    mathjaxtag1.attrs['type'] = 'text/x-mathjax-config' 
    mathjaxtag1.append(r"MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});")
    soup.head.insert(1, mathjaxtag1)
    with open(filename, "w") as outf:
        outf.write(str(soup))

def save_database(df, filename):    
    df.to_pickle(filename)
    
def load_database(filename):
    df = pd.read_pickle(filename)
    return(df)

def _make_clickable(val):
    # target _blank to open new window
    return '<a target="_blank" href="{}">{}</a>'.format(val, val)

# def _convert_time(val):
#     date = datetime.strptime(val,'%Y-%m-%dT%H:%M:%SZ')
#     return date.strftime("%Y-%m-%d %H:%M:%S")
# 
# def _remove_newlines(val):
#     return val.replace('\n  ', ' ')

def _make_utf8(val):
    return val.encode('utf-8')