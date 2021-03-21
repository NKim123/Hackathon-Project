from datetime import datetime
from datetime import timedelta
import time 

class Timer:
    target = None
    remaining = None

    def __init__(self, target):
        currentTime = datetime.now()
        now_str = currentTime
        now = datetime.strptime(now_str, '%H:%M')
        
        then_str = target.strftime("%H:%M")
        then = datetime.strptime(then_str, '%H:%M')
        time_delta= (then-now)
        total_seconds = time_delta.total_seconds()


        
        if self.total_seconds > 0:
            self.remaining = total_seconds
        print(self.remaining)

    def end():
        if currentTime > target:
            return True
        else:
            return False