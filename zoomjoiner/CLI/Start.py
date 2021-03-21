from ChromeJoinZoom import JoinZoom
import time
import datetime
def start():
    zoomLinks = [{"time1":"","link1":""},{"time2":"","link2":""},{"time3":"","link3":""},{"time4":"","link4":""}]
    print("Hello, just to get some things started:\n")
    username = input("School email?:\n")
    password = input("school password?:\n")
    time.sleep(2)
    for i in range(4):
        zoomLinks[i][f"link{i}"] = input(f"what is your period {i+1} link?\n")

    for i in range(4):
        yesno = input(f"join period{i+1}?(y/n):\n")
        if yesno == 'y':
            JoinZoom(zoomLinks[i][f"link{i}"], username=username, password=password)

start()