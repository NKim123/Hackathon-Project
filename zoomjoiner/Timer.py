from datetime import datetime
import time 

class Timer:
    currentTime = datetime.now()
    target = None
    remaining = None

    def __init__(self, target):
        self.target = target
        if self.currentTime < self.target:
            self.remaining = self.target - self.currentTime

    def end():
        if currentTime > target:
            return True
        else:
            return False