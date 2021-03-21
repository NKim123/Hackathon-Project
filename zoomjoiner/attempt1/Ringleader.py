
from Timer import Timer

class Ringleader:
    userInput = None
    

    def __init__(self, userInput):
        timerArray = []
        self.userInput = userInput
        for i in range(8):
            x=int((int(i)/2)+1)
            currentInput = userInput[f"{x}Time"]
            timerArray.append[Timer(currentInput)]
            i=i+1
        print(timerArray)

'''

if join button pressed:
    take all links and times save to variables 
    create all timer objects and put into array
    start timer1 for first time

for currentTimer in timerArray:
    while not currentTimer.end():
        time.sleep(1)

'''