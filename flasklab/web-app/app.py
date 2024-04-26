from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/rand')
def rand():
    name = random.choice(['Judy', 'Michael', 'Randy', 'Cal', 'Lucy', 'Susan'])
    adj = random.choice(['Wise', 'Brave', 'Inevitable', 'Unconventional', 'Wretched'])
    city = random.choice(['Seattle', 'Northfield', 'New York', 'San Fransisco', 'Houston', 'Miami', 'St. Louis'])
    year = random.randint(1900, 2024)
    return render_template("random.html", randName = name, randAdj = adj, randCity = city, randYear = year)

if __name__ == '__main__':
    my_port = 5131
    app.run(host='0.0.0.0', port = my_port) 
