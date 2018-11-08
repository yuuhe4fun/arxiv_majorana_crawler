# arxiv_majorana_crawler
For topo only

Goal: create & update an arxiv database of relevant papers (based on keywords, authors). If possible the database should be viewable for example via a browser, and it should be possible to notify users (for example via a weekly email) of new entries


Parts that go into this:
- Scraping the data from arxiv 
  - Arxiv api
  - Should follow arxiv rules
  - Have keywords/authors and such as input
  - Should run on a certain schedule
  - Could use urllib.requests to manually do so
  - Could use scrapy, which is more powerful but more complicated?
  
- Parsing the data into a database
  - Extract the relevant fields
  - Structure into a database
  - Could use feedparser, beautifulsoup, scrapy itself, other parsers..
  - What type of database to use? Pandas?
  
- Making the database accessibele 
  - What type of database to use?
  - Html?

- Notifying via email
  - On a schedule, check for new entries in some time range
  - Needs to be able to work with the database easily

