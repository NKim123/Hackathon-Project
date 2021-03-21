from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui
import cv2
import os
import time

def JoinZoom(link, username, password):

    currentFolder = os.getcwd()
    print(currentFolder)
    print("HERE\n\n\n\n\n")
    browser = webdriver.Chrome(f"{currentFolder}/chromedriver")

    # email
    browser.get("https://accounts.google.com/Login")
    usernameBox = browser.find_element_by_css_selector("#identifierId")
    usernameBox.send_keys(username)
    usernameBox.send_keys(Keys.ENTER)
    time.sleep(5)
    # password
    passwordBox = browser.find_element_by_css_selector("#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    passwordBox.send_keys(password)
    passwordBox.send_keys(Keys.ENTER)
    # opening signin
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get("https://zoom.us")
    browser.find_element_by_css_selector(".link").click()
    browser.find_element_by_css_selector("a.login-btn:nth-child(3)").click()
    # joining the meeting
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[2])
    browser.get(link)
    time.sleep(2)
    start = time.time()
    time.sleep(3)
    while True:
        var = pyautogui.locateOnScreen('open.png', confidence=0.6)
        if var != None:
            pyautogui.click(var)
            break
        var = pyautogui.locateOnScreen('openzoom.png', confidence=0.6)
        if var != None:
            pyautogui.click(var)
            break
        elif (time.time() - start) >= 120:
            print("link " + link + " not opened")
            break
        time.sleep(3)
    return

