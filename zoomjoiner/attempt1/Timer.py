from datetime import datetime
from datetime import timedelta
import time 

class Timer:
    target = None
    remaining = None

    def __init__(self, target):
        currentTime = datetime.now()
        now_str = currentTime
        now_str = str(now_str)
        now_str=(now_str[11:16])
        now = datetime.strptime(now_str, '%H:%M')
        
        
        then_str = target
        then = datetime.strptime(then_str, '%H:%M')
        time_delta= (then-now)
        total_seconds = time_delta.total_seconds()
        print(total_seconds)

        
        if total_seconds > 56:
            self.remaining = total_seconds
        else:
            self.remaining = 55;


        
    def getSeconds(self):
        return self.remaining

    def end():
        if currentTime > target:
            return True
        else:
            currentTime = datetime.now()
            return False