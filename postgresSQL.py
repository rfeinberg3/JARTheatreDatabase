# import library for python to postgreSQL connection
import psycopg2

# connect to databae server
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="", port=5433)

cur = conn.cursor()
########################################################################################################################

cur.execute("""CREATE TABLE IF NOT EXISTS Movies (
    MovieID VARCHAR(12),
    Name VARCHAR(50),
    Duration TIME,
    Director VARCHAR(50),
    Rated INTEGER,
    Rating INTEGER,
    is3D BOOLEAN
);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Theaters (
    TheaterCode VARCHAR(12),
    Address VARCHAR(100),
    Sponsor VARCHAR(50)
);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Rooms (
    TheaterCode VARCHAR(12) REFERENCES Theaters ON DELETE CASCADE,
    RoomID INTEGER,
    isXD BOOLEAN,
    Capacity INTEGER
);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS At (
    MovieID VARCHAR(12) REFERENCES Movies NOT NULL,
    TheaterCode INTEGER REFERENCES Theaters NOT NULL
);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Showing (
    MovieID VARCHAR(12) REFERENCES Movies NOT NULL,
    MovieName VARCHAR(50),
    Date DATE,
    StartTime TIME,
    TheaterCode VARCHAR(12) REFERENCES Theaters NOT NULL,
    RoomID VARCHAR(12) REFERENCES Rooms NOT NULL
);
""")

# cur.execute("""CREATE TABLE IF NOT EXISTS person (
#     id INT PRIMARY KEY,
#     name VARCHAR(255),
#     age INT,
#     gender CHAR
# );
# """)
#
# cur.execute(""" INSERT INTO person(id, name, age, gender) VALUES
#     (1, 'Mike', 30, 'm'),
#     (2, 'Lisa', 20, 'f'),
#     (3, 'Ryan', 22, 'm'),
#     (4, 'Natalie', 24, 'f');
# """)

# cur.execute(""" SELECT * FROM person WHERE name='Mike'; """)

# print(cur.fetchall())

########################################################################################################################

# commit changes to database
conn.commit()

# close cursor and database connection
cur.close()
conn.close()
