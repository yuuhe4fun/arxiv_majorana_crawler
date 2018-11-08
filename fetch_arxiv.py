import urllib
import feedparser

# Base api query url
base_url = 'http://export.arxiv.org/api/query?'

# Search parameters
search_query = 'all:majorana+AND+cat:cond-mat.mes-hall' 
# search for majorana in all fields and category cond-mat.mes-hall
start = 0                     # retreive the first 50 results
max_results = 50

query = 'search_query=%s&start=%i&max_results=%i' % (search_query,
                                                     start,
                                                     max_results)
sorting_order = '&sortBy=submittedDate&sortOrder=descending'

d = feedparser.parse(base_url+query+sorting_order)

for entry in d.entries:
    dic_stored = {}
    dic_stored['id'] = entry.id.split('/')[-1].split('v')[0]
    dic_stored['author_list'] = ', '.join([entry.authors[i]['name'] for i in range(len(entry.authors))])
    dic_stored['title'] = entry.title
    dic_stored['arxiv_primary_category'] = entry.arxiv_primary_category['term']
    dic_stored['published'] = entry.published
    dic_stored['link'] = entry.link

