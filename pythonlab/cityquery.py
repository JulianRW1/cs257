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
    if var == None:
        print('Northfield is not present in the database')
    else:
        print('Latitude: ' + str(var[3]) + ' Longitude: ' + str(var[4]))

    cur.execute("SELECT * FROM cities ORDER BY pop DESC")
    print('The city with the largest population is ' + str(cur.fetchone()[0]))

    cur.execute("SELECT * FROM cities WHERE state LIKE 'Minnesota' ORDER BY pop")
    print("Minnesota's smallest city is: " + str(cur.fetchone()[0]))

    # North, South, East, West most cities
    cur.execute("SELECT * FROM cities ORDER BY lat DESC LIMIT 1")
    north = str(cur.fetchone()[0])

    cur.execute("SELECT * FROM cities ORDER BY lat LIMIT 1")
    south = str(cur.fetchone()[0])

    cur.execute("SELECT * FROM cities ORDER BY long DESC LIMIT 1")
    east = str(cur.fetchone()[0])

    cur.execute("SELECT * FROM cities ORDER BY long LIMIT 1")
    west = str(cur.fetchone()[0])

    print("Furthest North: " + north + 
          " \nFurthest East" + east +
          " \nFurthest South" + south +
          " \nFurthest West" + west )
    
    # user input
    state = input('Enter a state: ')

    #look up in abbreviations table
    cur.execute("SELECT * FROM states WHERE code LIKE '" + state.upper() + "'")
    
    var = cur.fetchone()
    if var != None:
        state = str(var[1])

    print(var)
    print('state: ' + state)

    cur.execute("SELECT * FROM cities WHERE state LIKE '" + state + "'")

    all_cities = cur.fetchall()
    
    total_population = 0
    for city in all_cities:
        total_population += city[2]

    print('total population: ' + str(total_population))
        

    conn.commit()


query()
