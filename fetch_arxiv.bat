@echo on
call E:\Programs\Anaconda3\Scripts\activate.bat
CD /D E:\Code\arxiv_majorana_crawler
E:\Programs\Anaconda3\python.exe "fetch_arxiv.py"