import time
import fetch_arxiv

cycletime = 60*60*6 # s * min * h

doLooping = True
while doLooping:
    try:
        while True: #keep uploading stuff
            print('===')
            fetch_arxiv.main(debug_mode=True)
            time.sleep(cycletime)
    except KeyboardInterrupt:
        print('shutting down nicely')
        doLooping = False
    # except:
    #    print('Something else srewed up')
    #    time.sleep(cycletime)
print('Done')
