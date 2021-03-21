from flask import Flask, redirect, url_for, render_template, request
from ChromeJoinZoom import JoinZoom
from selenium.webdriver import Chrome
from selenium import webdriver
app = Flask(__name__)
userInfo = None

@app.route("/")
def home():
    return render_template("JoinPage.html")

@app.route("/", methods = ['POST'])
def data(): 
    if request.method == 'POST':
        print('worked')
        userInfo = request.form
        print(userInfo)
        driver = webdriver.Chrome("C:/Users/mikim/OneDrive/Documents/GitHub/Hackathon-Project/zoomjoiner/attempt1/chromedriver.exe")
        driver.get("https://google.com")
        return render_template("Success.html")

if __name__=="__main__":
    app.run(debug=True)