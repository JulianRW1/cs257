import psycopg2

def city_queries():
    
    conn = psycopg2.connect(
      host="localhost",
      port=5432,   
      database="walstonj",
      user="walstonj",
      password="tablet995sunshine")
    
    cur = conn.cursor()

    # 1. check for Northfield
    cur.execute("SELECT * FROM cities WHERE city LIKE 'Northfield';")
    temp = cur.fetchone()
    if temp == None:
        print('Northfield is not present in the database\n')
    else:
        print('Latitude: ' + str(temp[3]) + ' Longitude: ' + str(temp[4]) +'\n')

    # 2. Find the city with the largest population
    cur.execute("SELECT * FROM cities ORDER BY pop DESC")
    print('The city with the largest population is ' + str(cur.fetchone()[0])+'\n')

    # 3. Find the smallest city in Minnesota
    cur.execute("SELECT * FROM cities WHERE state LIKE 'Minnesota' ORDER BY pop")
    print("Minnesota's smallest city is: " + str(cur.fetchone()[0]) +'\n')

    # 4. Find the cities furthest North, South, East, and West
    cur.execute("SELECT * FROM cities ORDER BY lat DESC LIMIT 1")
    north = str(cur.fetchone()[0])

    cur.execute("SELECT * FROM cities ORDER BY lat LIMIT 1")
    south = str(cur.fetchone()[0])

    cur.execute("SELECT * FROM cities ORDER BY long DESC LIMIT 1")
    east = str(cur.fetchone()[0])

    cur.execute("SELECT * FROM cities ORDER BY long LIMIT 1")
    west = str(cur.fetchone()[0])

    print("Furthest North: " + north + 
          "\nFurthest East: " + east +
          "\nFurthest South: " + south +
          "\nFurthest West: " + west +'\n')
    
    state = input('Enter a state: ').capitalize()

    cur.execute("SELECT * FROM states WHERE code LIKE '" + state.upper() + "'")
    temp = cur.fetchone()
    
    if temp != None:
        state = str(temp[1])

    cur.execute("SELECT * FROM cities WHERE state LIKE '" + state + "'")
    all_cities = cur.fetchall()
    
    if all_cities == None:
        print(state + ' is not in the database')
    else:
      total_population = 0
      for city in all_cities:
          total_population += city[2]
      print('total population: ' + str(total_population))

    conn.commit()


city_queries()
