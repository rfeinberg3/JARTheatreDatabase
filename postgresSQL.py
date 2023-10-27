# import library for python to postgreSQL connection
import psycopg2

# connect to databae server
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="", port=5433)

cur = conn.cursor()
########################################################################################################################

# initiate tables if they don't exist
cur.execute(open("Tables.sql", "r").read())

### run to initiate values 
#cur.execute(""" INSERT INTO Staff(StaffID, Name, Email, PhoneNumber) VALUES
            #(1111111111, 'Ryan', 'rfein@gmail.com', 561);  """)
## commit changes to database
#conn.commit()

def main_page():
    userInput = -1
    while(userInput!=0):
        print("\n\n##################################")
        print("Welcome to JAR, where movies are.")
        print("##################################")
        print("Navigations: ")
        print("1.  Member Login <-- Under Construction")
        print("2.  Employee Login <-- Under Construction")
        print("3.  Admin Login")
        print("4.  About JAR <-- Under Construction")
        print("0.  Exit")

        userInput = int(input("Please select by entering one of digits 1-4: "))
        while(userInput < 0 or userInput > 4):
            print("---> Invalid selection <---")
            userInput = int(input("Please select by entering one of digits 1-4: "))

        if userInput == 1:
            member_page()
        if userInput == 2:
            employee_page()
        if userInput == 3:
            admin_page()
        if userInput == 4:
            about_page()
        if userInput == 0:
            print("Exiting program... Goodbye :)")



def member_page():
    " create member login "
    #table = input("Table name: ")
    #values = []
    #values.append(input("Value tuple {}: ".format(iteration)))
    ## from table and values create an sql query
    pass

def employee_page():
    " create employee login "
    pass

def admin_page():
    " create admin login "
    userInput = -1
    while(userInput!=0):
        print("\n\n##################################")
        print("Administrative page. All funtionality available")
        print("Navigations: ")
        print("1.  INSERT")
        print("2.  SELECT")
        print("3.  DELETE")
        print("0.  Exit page")

        # make a selection
        userInput = int(input("Selection: "))
        while(userInput < 0 or userInput > 3):
            print("---> Invalid selection <---")
            userInput = int(input("Selection: "))
        
        # selections...
        if userInput == 1: # INSERT
            command = input("postgreSQL INSERT: ")
            string = """ {} """.format(command)
            cur.execute(string)
            conn.commit()  # commit changes to databaseß

        if userInput == 2: # SELECT
            command = input("postgreSQL SELECT query: ")
            string = """ {} """.format(command)
            cur.execute(string)
            for row in cur.fetchall(): # print statement results
                print(row) 

        if userInput == 3: # DELETE
            command = input("postgreSQL SELECT query: ")
            string = """ {} """.format(command)
            userInput = input("Are you sure you want to delete? Enter 'DELETE' if so: ")
            if userInput == "DELETE":
                cur.execute(string)
                conn.commit()  # commit changes to databaseß
            else:
                userInput = -1
                print("Redirecting...")
        if userInput == 0: # Exit 
            print("Returning to main page...\n\n")

def about_page():
    pass

### Main ###
####################
main_page()
####################
### End Main ###

'''
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
'''

########################################################################################################################

# commit changes to database
conn.commit()

# close cursor and database connection
cur.close()
conn.close()
