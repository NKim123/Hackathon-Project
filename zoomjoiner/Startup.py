from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("JoinPage.html")

@app.route("/", method = ['GET'])
def data(): 
    if request.method == 'GET':
        print('worked')

if __name__=="__main__":
    app.run(debug=True)