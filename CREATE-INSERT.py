# import library for postgreSQL connection
import psycopg2

# connect to database server
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="database_design", port=5433)
# create cursor to database
cur = conn.cursor()

########################################################################################################################


# initiate tables in database if they don't exist
cur.execute(open("/Users/ryan/Desktop/Database Design/FinalProjectCollection/MovieTheaterDB/Tables.sql", "r").read())
conn.commit()


# insert into or update values in database
cur.execute(open("/Users/ryan/Desktop/Database Design/FinalProjectCollection/MovieTheaterDB/Inserts.sql", "r").read())
conn.commit()


print("CREATE-INSERT complete")

########################################################################################################################
# close cursor and database connection
cur.close()
conn.close()


