from flask import Flask, redirect, url_for, render_template, request
from selenium import Chrome

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
        
        return render_template("Success.html")

if __name__=="__main__":
    app.run(debug=True)