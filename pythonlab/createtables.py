import psycopg2

def create_tables():
    
  conn = psycopg2.connect(
      host="localhost",
      port=5432,   
      database="walstonj",
      user="walstonj",
      password="tablet995sunshine")

  cur = conn.cursor()

  cities = """CREATE TABLE DROP TABLE IF EXISTS cities;
    CREATE TABLE cities (
      code text,
      state text,
      pop real
    );"""

  states = """CREATE TABLE DROP TABLE IF EXISTS states;
    CREATE TABLE states (
      city text,
      state text,
      pop real,
      lat real,
      long real
    );""" 
  cur.execute(cities)
  cur.execute(states)

create_tables()
