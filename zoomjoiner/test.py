from datetime import datetime
import time

time1 = datetime.now()
time.sleep(3)
time2 = datetime.now()

time3 = time2 - time1

print(time3.seconds)