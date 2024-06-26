import flask
import psycopg2

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Red">' + word1 + '</h1>'

@app.route('/add/<num1>/<num2>')
def add(num1, num2):
    return str(int(num1) + int(num2))

@app.route('/pop/<abbr>')
def get_population(abbr):
    conn = psycopg2.connect(
      host="localhost",
      port=5432,
      database="walstonj",
      user="walstonj",
      password="tablet995sunshine")

    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE code LIKE '" + abbr.upper() + "';")
    pop = cur.fetchone()[2]
    conn.commit()
    return str(pop)

if __name__ == '__main__':
    my_port = 5131
    app.run(host='0.0.0.0', port = my_port) 
