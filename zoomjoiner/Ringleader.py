
from zoomjoiner.Timer import Timer

class Ringleader:
    userInput = None
    timerArray = []

    def __init__(self, userInput):
        self.userInput = userInput
        for i in range(4):
            currentInput = userInput[f"class{i}time"]
            timerArray.append[Timer()]


'''

if join button pressed:
    take all links and times save to variables 
    create all timer objects and put into array
    start timer1 for first time

for currentTimer in timerArray:
    while not currentTimer.end():
        time.sleep(1)

'''