@echo on
call E:\ProgramData\Anaconda3\Scripts\activate.bat
CD /D D:\Beihang_University\arxiv_majorana_crawler
E:\ProgramData\Anaconda3\python.exe "fetch_arxiv.py" "config_mac.json"