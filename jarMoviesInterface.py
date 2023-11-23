# import library for postgreSQL connection
import psycopg2
import random

# connect to database server
conn = psycopg2.connect(host="localhost", dbname="jarMovies", user="postgres", password="database_design", port=5433)

# create cursor to database
cur = conn.cursor()
########################################################################################################################


def main_page():
    userInput = -1
    while(userInput!=0):
        print("\n\n##################################")
        print("Welcome to JAR, where movies are.")
        print("##################################")
        print("Navigations: ")
        print("1.  Member Login")
        print("2.  Admin Page")
        print("3.  About JAR <-- Under Construction")
        print("0.  Exit")

        # check user input
        userInput = int(input("Please select by entering one of digits 0-3: "))
        while(userInput < 0 or userInput > 3):
            print("---> Invalid selection <---")
            userInput = int(input("Please select by entering one of digits 0-3: "))

        # page transitions:
        if userInput == 1:
            member_login()
        if userInput == 2:
            admin_page()
        if userInput == 3:
            about_page()
        if userInput == 0:
            print("Exiting program... Goodbye :)")



def member_login():
    # member login/signup *
    userInput = -1
    while(userInput!=0):
        print("\n\n##################")
        print("Member SignUp/Login")
        print("##################")
        print("Navigations: ")
        print("1.  Sign Up")
        print("2.  Login")
        print("0.  Exit")

        # check user input
        userInput = int(input("Please select by entering one of digits 0-2: "))
        while(userInput < 0 or userInput > 2):
            print("---> Invalid selection <---")
            userInput = int(input("Please select by entering one of digits 0-2: "))

       # page transitions:
        if userInput == 1: # signup <------
            # get username and password (iterates until user confirms their username and password is entered correctly)
            userInput = -1
            while(userInput!=1): 
                name = input("Enter your full name: ")
                email = input("Enter an email address: ")
                password = input("Enter a password: ")
                MemberID = str(random.randint(999999999, 9999999999))
                userInput = int(input("Is name: {}, email: {}, and password: {} correct? (1=yes, 0=no): ".format(name, email, password)))
            print("Creating Account...")
            print("Account created with Member ID: {}".format(MemberID))
            cur.execute(''' INSERT INTO Customers(MemberID, Password, Points, Name, Email) VALUES({}, '{}', 0, '{}', '{}' ) '''.format(MemberID, password, name, email))
            conn.commit()
            print("Account Created... Redirecting to login page...")
            userInput = 2

        if userInput == 2: # login <------
            userInput = -1
            # get username and password (iterates until user confirms their username and password is entered correctly)
            print("##################\n##################")
            print("Login: ")
            loginValid = False

            # user input
            email = str(input("Enter an email address: "))
            password = str(input("Enter a password: "))

            # find user
            cur.execute(
                ''' SELECT MemberID, Email, Password FROM Customers WHERE Email = '{}' AND Password = '{}'; '''.format(email, password)
                )
            for row in cur.fetchall():
                MemberID = row[0]
                loginValid = True #  if there is a value in cursor, this means an account has been found. Set loginValid to true.
            if loginValid:
                userInput = 0 # set to 0 to return to main page when logout occurs (see while loop)
                member_portal(MemberID)# call member page
            else:
                print("Login details invalid. Returning to Navigation Page...")

        if userInput == 0:
            print("Returning to main page... ")

# end of member_login()

def employee_page():
    " create employee login maybe"
    pass

def admin_page():
    # welcome interface
    userInput = -1
    while(userInput!=0):
        print("\n\n##################################")
        print("Administrative page. All funtionality available")
        print("Navigations: ")
        print("1.  INSERT")
        print("2.  SELECT")
        print("3.  DELETE")
        print("4.  Advanced Queries")
        #print("5.  Customer Information")
        #print("6.  Theater Information")
        print("0.  Back")

        # make a selection
        userInput = int(input("Selection: "))
        while(userInput < 0 or userInput > 4):
            print("---> Invalid selection <---")
            userInput = int(input("Selection: "))
        
        # selections:
        if userInput == 1: # INSERT
            command = input("postgreSQL INSERT: ")
            string = """ {} """.format(command)
            cur.execute(string)
            conn.commit()  # commit changes to database

        if userInput == 2: # SELECT
            command = input("postgreSQL SELECT query: ")
            string = """ {} """.format(command)
            cur.execute(string)
            for row in cur.fetchall(): # print statement results
                print(row) 

        if userInput == 3: # DELETE
            command = input("postgreSQL DELETE query: ")
            string = """ {} """.format(command)
            userInput = input("Are you sure you want to delete? Enter 'DELETE' if so: ")
            if userInput == "DELETE":
                cur.execute(string)
                conn.commit()  # commit changes to database
            else:
                userInput = -1
                print("Redirecting...")

        if userInput == 4: # Advanced Queries
            print("\n##################################")
            print("Advanced Query Selection:")
            print("1...")
            print("2...")
            command = int(input("Would you like to see a specific employees info? (enter 1, or enter 0 to see all): "))
            if command:
                empName = input("Enter employee's name: ")
                cur.execute(''' SELECT * FROM Staff WHERE Name = '{}'; '''.format(empName))
            else:
                cur.execute(''' SELECT * FROM Staff; ''')
            print("##################################")
            for row in cur.fetchall():
                name = row[1]
                email = row[2]
                phone = row[3]
                print("Employee Name: {} ---> Email: {}, Phone#: {}".format(name, email, phone))

        if userInput == 0: # Exit 
            print("Returning to main page...\n\n")
# end of admin_page()

def about_page():
    pass

def member_portal(MemberID):
    userInput = -1
    while(userInput!=0):
        print("\n\n##################")
        print("Greetings JAR Member!!!")
        print("##################")
        print("Navigations: ")
        print("1.  See Profile")
        print("2.  Change Email or Password <--- Under Construction")
        print("3.  See Points")
        print("4.  See Purchased Tickets <--- Under Construction")
        print("5.  Browse Movies")
        print("0.  Logout")
        # check user input
        userInput = int(input("Please select by entering one of digits 0-5: "))
        while(userInput < 0 or userInput > 5):
            print("---> Invalid selection <---")
            userInput = int(input("Please select by entering one of digits 0-5: "))

        if userInput == 1: #  See Profile
            cur.execute(''' SELECT Name, Email, Password FROM Customers WHERE MemberID = '{}';'''.format(MemberID))
            output = cur.fetchall()
            name = output[0][0]
            email = output[0][1]
            password = output[0][2]
            print("Name: {}\nEmail: {}\nPassword: {}".format(name, email, password))
        
        if userInput == 2: #  Change Email or Password
            continue
        if userInput == 3: #  See Points
            cur.execute(''' SELECT Points FROM Customers WHERE MemberID = '{}'; '''.format(MemberID))
            output = cur.fetchall()
            points = output[0][0]
            print("JAR Point Total: {}".format(points))

        if userInput == 4: #  See Purchased Tickets
            cur.execute(f''' SELECT Name, Duration, Director, Rated, Rating, is3D 
                             FROM Showing, Movies, Tickets WHERE TicketPurchaser = '{MemberID}' 
                                AND Tickets.Showing = Showing.ShowingID 
                                AND Showing.MovieID = Movies.MovieID;''')
            for row in cur.fetchall():
                name = row[0]
                dur = row[1]
                dir = row[2]
                rated = row[3]
                if rated:
                    rating = row[4]
                else:
                    rating = "Not Rated"
                is3D = row[5]
                print("Ticket Purchased for -----  Movie: {} ---> Duration: {} -- Director: {} -- Rating: {} -- Movie in 3D: {}".format(name, dur, dir, rating, is3D))
        

        if userInput == 5: #  Browse Movies
            cur.execute(''' SELECT MovieID, Name, Duration, Director, Rated, Rating, is3D FROM Movies;''')
            movies = cur.fetchall()
            for row in movies:
                id = row[0]
                name = row[1]
                dur = row[2]
                dir = row[3]
                rated = row[4]
                if rated:
                    rating = row[5]
                else:
                    rating = "Not Rated"
                is3D = row[6]
                print("ID: {} ---> Movie: {} ---> Duration: {} -- Director: {} -- Rating: {} -- Movie in 3D: {}".format(id, name, dur, dir, rating, is3D))
            userInput = int(input("Enter the name an ID to buy a ticket (or 0 to cancel): "))
            if userInput:
                for movie in movies:
                    if int(movie[0]) == userInput:
                        movieName = movie[1]
                ticketID = str(random.randint(9999999, 99999999))
                price = 6
                purchaser = MemberID
                roomID = 2222
                seat = 9
                row = 'B'
                cur.execute(''' SELECT ShowingID FROM Showing WHERE MovieID = '{}'; '''.format(userInput))
                output = cur.fetchall()
                Showing = output[0][0]
                cur.execute(''' INSERT INTO Tickets(TicketID, Showing, Price, TicketPurchaser, RoomID, Seat, Row)
	                            VALUES ({}, {}, {}, {}, {}, {}, '{}');   
                            '''.format(ticketID, Showing, price, purchaser, roomID, seat, row))
                conn.commit()
                print("Congrats!!! Your ticket for {} has been purchased!!!".format(movieName))
            userInput = -1

        if userInput == 0: #  Logout ---> returns user to main_page()
            print("Logging out...")
# end member_portal()

### Main ###
####################

# initiate program
main_page()

# close cursor and database connection
cur.close()
conn.close()

####################
### End Main ###
