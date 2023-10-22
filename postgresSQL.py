# import library for python to postgreSQL connection
import psycopg2

# connect to databae server
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="", port=5433)

cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS person (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender CHAR
);
""")

cur.execute(""" INSERT INTO person(id, name, age, gender) VALUES 
    (1, 'Mike', 30, 'm'),
    (2, 'Lisa', 20, 'f'),
    (3, 'Ryan', 22, 'm'),
    (4, 'Natalie', 24, 'f');
""")

cur.execute(""" SELECT * FROM person WHERE name='Mike'; """)

print(cur.fetchall())


# commit changes to database
conn.commit()

# close cursor and database connection
cur.close()
conn.close()
