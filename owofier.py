import random

#changes an input message into the "owo" style 
def owofier(message):
    allChanged = False
    returnMessage = message

    #while loop goes through the message and changes all instances of specific letters to conform with "owo" style words
    while not allChanged:

        #Finds the index of each instance 
        rIndex = returnMessage.find("r")
        lIndex = returnMessage.find("l")
        theIndex = returnMessage.find("the")
        TheIndex = returnMessage.find("The")
        IIndex = returnMessage.find("I ")
        thIndex = returnMessage.find("th")
        owoUwu = random.randint(0,1)
        if rIndex != -1:
            returnMessage = returnMessage[0:rIndex] + "w" + returnMessage[rIndex+1:]
        if lIndex != -1:
            returnMessage = returnMessage[0:lIndex] + "w" + returnMessage[lIndex+1:]
        if thIndex != -1:
            returnMessage = returnMessage[0:thIndex] + "f" + returnMessage[thIndex+1:]
        if theIndex != -1:
            returnMessage = returnMessage[0:theIndex] + "da" + returnMessage[theIndex+3:]
        if TheIndex != -1:
            returnMessage = returnMessage[0:TheIndex] + "Da" + returnMessage[TheIndex+3:]
        if IIndex != -1:
            returnMessage = returnMessage[0:IIndex] + "me" + returnMessage[IIndex+1:]
        if rIndex == -1 and lIndex == -1 and theIndex == -1 and IIndex == -1:
            allChanged = True

    #adds an extra owo or uwu to the end of each tweet
    if owoUwu == 1:
        returnMessage += " owo >:3"
    elif owoUwu == 0:
        returnMessage += " uwu :3"

    return returnMessage

print(owofier("Hello all. Gini Khalsa here from NIST/NCCoE. I'm an IT Specialist focusing on computer infrastructure and am a mentor for NIST's summer high school internship program (SHIP) where we have 8-week internships for juniors and seniors as well as the NIST student volunteer program (SVP) which is based on a term agreed between you and NIST."))
