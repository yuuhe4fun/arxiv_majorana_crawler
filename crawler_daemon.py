import time
import fetch_arxiv

cycletime = 60*60*24 # every day

doLooping = True
while doLooping:
    try:
        while True: #keep uploading stuff
            fetch_arxiv.main()
            time.sleep(cycletime)
    except KeyboardInterrupt:
        print('shutting down nicely')
        doLooping = False
    # except:
    #    print('Something else srewed up')
    #    time.sleep(cycletime)
print('Done')
