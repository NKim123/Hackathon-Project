
from Timer import Timer
import time
from ChromeJoinZoom import JoinZoom
from selenium.webdriver import Chrome
from selenium import webdriver
from flask import Flask, redirect, url_for, render_template, request

class Ringleader:
    userInput = None
    

    def __init__(self, userInput):
        timer = None
        link = None
        self.userInput = userInput

        for i in range(4):
            timerCounter=i+1
            timeInput = userInput[f"{timerCounter}Time"]
            linkCounter=i+1
            link = userInput[f"{linkCounter}Link"]
            timer =Timer(timeInput)
            print("URMOMRUMOMRURMOMRURMOM")
            time.sleep(timer.getSeconds()-55)
            JoinZoom(link,"244388", "nhEC@rr3G.5ZCC%")
            '''
            driver = webdriver.Chrome("C:/Users/noahk/Documents/GitHub/Hackathon-Project/zoomjoiner/attempt1/chromedriver.exe")
            print(link)
            driver.get(link)
            '''
    def prettywebpage():
        return render_template("Success.html");
'''

if join button pressed:
    take all links and times save to variables 
    create all timer objects and put into array
    start timer1 for first time

for currentTimer in timerArray:
    while not currentTimer.end():
        time.sleep(1)

'''