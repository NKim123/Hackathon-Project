from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui

import time

def JoinZoom(link):
    username = "244388@mcpsmd.net"
    password = "asdfghjkl;'"
    browser = webdriver.Chrome("/Users/noahkim/Documents/chromedriver")
    #chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--disable-default-apps")
    #browser = webdriver.Chrome("/Users/noahkim/Documents/chromedriver", options=chrome_options)

    #email
    browser.get("https://accounts.google.com/Login")
    usernameBox = browser.find_element_by_css_selector("#identifierId")
    usernameBox.send_keys(username)
    usernameBox.send_keys(Keys.ENTER)
    time.sleep(2)
    #password
    passwordBox = browser.find_element_by_css_selector("#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    passwordBox.send_keys(password)
    passwordBox.send_keys(Keys.ENTER)
    #time.sleep(2)
    #opening signin
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    #time.sleep(2)
    browser.get("https://zoom.us")
    browser.find_element_by_css_selector(".link").click()
    #time.sleep(2)
    browser.find_element_by_css_selector("a.login-btn:nth-child(3)").click()
    #joining the meeting
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[2])
    browser.get(link)
    
    time.sleep(2)
    print("something")
    buttonLoc = pyautogui.locateOnScreen('openzoom.png')
    print(buttonLoc)
    print("something2")
    pyautogui.Click(buttonLoc)

    '''
    I want it to accept the dialogue box here
    '''

    #this is just to keep the window open for now
    while(True):
       pass


JoinZoom("https://mcpsmd.zoom.us/j/97130321813?pwd=cW9tYU9wVjV5c3hKbEZsU0FwalAxUT09")