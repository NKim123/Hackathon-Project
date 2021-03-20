import random

def owofier(message):
    allChanged = False
    returnMessage = message
    while not allChanged:
        rIndex = returnMessage.find("r")
        lIndex = returnMessage.find("l")
        theIndex = returnMessage.find("the")
        IIndex = returnMessage.find("I")
        owoUwu = random.randint(0,1)
        if rIndex != -1:
            returnMessage = returnMessage[0:rIndex] + "w" + returnMessage[rIndex+1:]
        if lIndex != -1:
            returnMessage = returnMessage[0:lIndex] + "w" + returnMessage[lIndex+1:]
        if theIndex != -1:
            returnMessage = returnMessage[0:theIndex] + "da" + returnMessage[theIndex+3:]
        if IIndex != -1:
            returnMessage = returnMessage[0:IIndex] + "me" + returnMessage[IIndex+1:]
        if rIndex == -1 and lIndex == -1 and theIndex == -1 and IIndex == -1:
            allChanged = True

    if owoUwu == 1:
        returnMessage += " owo >:3"
    elif owoUwu == 0:
        returnMessage += " uwu :3"

    return returnMessage

print(owofier("My team and I are building an organizational/grades app for students. I was wondering if you would be interested in joining a call with my and my teammates to give us some insight based on your past experiences as a teacher."))