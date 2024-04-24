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
    print('nofo: ' + cur.fetchone())

    cur.execute("""SELECT * FROM cities WHERE city LIKE 'Seattle';""")
    print('seattle: ' + cur.fetchone())
    # cur.execute()
    # cur.fetchone()
    conn.commit()


query()
