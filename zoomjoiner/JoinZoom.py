from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

def JoinZoom(link):
    username = "244388@mcpsmd.net"
    password = "asdfghjkl;'"
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.headless = True
    browser = webdriver.Firefox()

    browser.get("https://accounts.google.com/Login")
    usernameBox = browser.find_element_by_css_selector("#identifierId")
    usernameBox.send_keys(username)
    usernameBox.send_keys(Keys.ENTER)
    time.sleep(1)
    passwordBox = browser.find_element_by_css_selector("#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    passwordBox.send_keys(password)
    passwordBox.send_keys(Keys.ENTER)
    time.sleep(1)
    
    browser.get(link)

JoinZoom("https://mcpsmd.zoom.us/j/97130321813?pwd=cW9tYU9wVjV5c3hKbEZsU0FwalAxUT09")