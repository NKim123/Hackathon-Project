from flask import Flask, redirect, url_for, render_template, request
<<<<<<< HEAD
from selenium import Chrome

=======
from ChromeJoinZoom import JoinZoom
from selenium.webdriver import Chrome
from selenium import webdriver
from Ringleader import Ringleader
>>>>>>> f1228e2b68a7e967c1e10bd883c2f9fd5e14d3c4
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
<<<<<<< HEAD
        
        return render_template("Success.html")
=======
        print(userInfo)
        smile=Ringleader.prettywebpage()
        ringleader=Ringleader(userInfo)


def smiles():
	return render_template("Success.html");
        
>>>>>>> f1228e2b68a7e967c1e10bd883c2f9fd5e14d3c4

if __name__=="__main__":
    app.run(debug=True)