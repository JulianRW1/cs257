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

    cur.execute("""SELECT * FROM cities WHERE city LIKE 'Northfield';""")
    var = cur.fetchone()
    if (var == None):
        print('Northfield is not present in the database')
    else:
        print(var)

    cur.execute("""SELECT * FROM cities WHERE city LIKE 'Seattle';""")
    var = cur.fetchone()
    if (var == None):
        print('Seattle is not present in the database')
    else:
        print('Latitude: ' + var.lat + ' Longitude: ' + var.long)

    conn.commit()


query()
