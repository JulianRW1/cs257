import psycopg2

def query():
    
    conn = psycopg2.connect(
      host="localhost",
      port=5432,   
      database="walstonj",
      user="walstonj",
      password="tablet995sunshine")
    
    cur = conn.cursor()
    
    states = """DROP TABLE IF EXISTS states;
    CREATE TABLE states (
      code text,
      state text,
      pop real
    );"""
    
    cities = """DROP TABLE IF EXISTS cities;
    CREATE TABLE cities (
      city text,
      state text,
      pop real,
      lat real,
      long real
    );""" 

    cur.execute("SELECT * FROM cities WHERE city LIKE 'Northfield';")
    var = cur.fetchone()
    if (var == None):
        print('Northfield is not present in the database')
    else:
        print('Latitude: ' + str(var[3]) + ' Longitude: ' + str(var[4]))

    cur.execute("SELECT * FROM cities ORDER BY pop DESC")
    print('The city with the largest population is ' + str(cur.fetchone()[0]))

    cur.execute("SELECT * FROM cities WHERE state LIKE 'Minnesota' ORDER BY pop")
    print("Minnesota's smallest city is: " + str(cur.fetchone()[0]))
    
    conn.commit()


query()
