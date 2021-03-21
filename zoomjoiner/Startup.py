from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("JoinPage.html")

@app.route("/", methods = ['POST'])
def data(): 
    if request.method == 'POST':
        print('worked')
        return render_template("JoinPage.html")


if __name__=="__main__":
    app.run(debug=True)