@echo on
call C:\Users\guanzhongwang\AppData\Local\Continuum\anaconda3\Scripts\activate.bat
CD /D E:\Code\arxiv_majorana_crawler
C:\Users\guanzhongwang\AppData\Local\Continuum\anaconda3\python.exe "fetch_arxiv.py"
