
def owofier(message):
    allChanged = False
    returnMessage = message
    while not allChanged:
        rIndex = message.find("r")
        lIndex = message.find("l")
        thIndex = message.find("th")
        theIndex = message.find(" the ")
        IIndex = message.find(" I ")
        if rIndex != -1:
            returnMessage = returnMessage[0:rIndex] + "w" + returnMessage[rIndex+1:]
        if lIndex != -1:
            returnMessage = returnMessage[0:lIndex] + "w" + returnMessage[lIndex+1:]
        if thIndex != -1:
            returnMessage = returnMessage[0:thIndex] + "w" + returnMessage[thIndex+1:]
        if theIndex != -1:
            returnMessage = returnMessage[0:theIndex] + "w" + returnMessage[theIndex+1:]
        if IIndex != -1:
            returnMessage = returnMessage[0:IIndex] + "w" + returnMessage[IIndex+1:]
        if rIndex == -1 and lIndex == -1 and thIndex == -1 and theIndex == -1 and IIndex == -1:
            allChanged = True

    return returnMessage

owofier("46th President of the United States, husband to @FLOTUS, proud dad & pop. Tweets may be archived")