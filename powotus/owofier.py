import random
import re
#changes an input message into the "owo" style 
def owofier(message):
    allChanged = False
    returnMessage = message

    #while loop goes through the message and changes all instances of specific letters to conform with "owo" style words
    owoUwu = random.randint(0,1)
    returnMessage = re.sub(r'(wr|r|l)', 'w', returnMessage, flags=re.IGNORECASE)
    returnMessage = re.sub(r'the\W', 'de ', returnMessage, flags=re.IGNORECASE)
    returnMessage = re.sub(r'\WI\W',' me ', returnMessage, flags=re.IGNORECASE)
    returnMessage = re.sub(r'th', 'v', returnMessage, flags=re.IGNORECASE)

    #adds an extra owo or uwu to the end of each tweet
    if owoUwu == 1:
        returnMessage += " owo >:3"
    elif owoUwu == 0:
        returnMessage += " uwu :3"

    return returnMessage

print(owofier("The Georgia voting law — like so many others being pursued by Republicans in statehouses across the country — is a blatant attack on the right to vote, the Constitution, and good conscience. It’s Jim Crow in the 21st Century — and it must end."))
