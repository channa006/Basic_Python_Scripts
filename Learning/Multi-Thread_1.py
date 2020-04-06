import threading
import time
from datetime import datetime


startTime = datetime.now()


def runtheprogram():
    print('Program is Running')
    time.sleep(3)
    print('Program is Stopping')


threads = []

for i in range(5):
    t = threading.Thread(target=runtheprogram)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("\nTotal execution time:")
print(datetime.now() - startTime)
