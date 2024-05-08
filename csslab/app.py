from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/random-number')
def randomNumberGenerator():
    return render_template("randomNumber.html")

@app.route('/change-color')
def changeColor():
    return render_template("changeColor.html")

if __name__ == '__main__':
    my_port = 5000
    app.run(host='0.0.0.0', port = my_port) 

