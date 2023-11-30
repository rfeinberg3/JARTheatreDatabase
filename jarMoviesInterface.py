# import library for postgreSQL connection
import psycopg2
import random

# connect to database server
conn = psycopg2.connect(host="localhost", dbname="", user="postgres", password="database_design", port=5433)

# create cursor to database
cur = conn.cursor()
########################################################################################################################

INJECTIONCHARS = [',', '\'', '-', '#', ';'] # Characters that could be used for SQL injection attacks, which should be omitted from any inputs

def main_page():
    userInput = -1
    while(userInput!=0):
        print("\n\n##################################")
        print("Welcome to JAR, where movies are.")
        print("##################################")
        print("Navigations: ")
        print("1.  Member Login")
        print("2.  Admin Page")
        print("3.  About JAR")
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
                # Injection attack check
                if userInput:
                    for CHAR in INJECTIONCHARS:
                        if ((CHAR in name) or (CHAR in email) or (CHAR in password)):
                            print(f"Invalid character = {CHAR}\nReturning to Main Page...")
                            return
            # Account creation valid
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
            # Injection attack check
            for CHAR in INJECTIONCHARS:
                if ((CHAR in email) or (CHAR in password)):
                    print(f"Invalid character = {CHAR}\nReturning to Main Page...")
                    return

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
                userInput = -1

        if userInput == 0:
            print("Returning to main page... ")

# end of member_login()


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
            print("1.  What Theater(s) Does an Employee Work At?")
            print("2.  What Have Customers Been Eating?")
            print("0.  Back")

            # make a selection
            userInput = int(input("Selection: "))
            while(userInput < 0 or userInput > 2):
                print("---> Invalid selection <---")
                userInput = int(input("Selection: "))

            if userInput == 1: # Advanced Query 1
                empName = input("Enter employee's name: ") # ask for user to input employees name
                # Test for invalid characters
                for CHAR in INJECTIONCHARS:
                    if CHAR in empName:
                        print(f"Invalid character = {CHAR}\nReturning to Main Page...")
                        return
                # Execute Statement
                cur.execute(''' SELECT Theaters.TheaterCode, Address, Sponsor 
                                FROM Staff, ScheduledAt, Theaters
                                WHERE Name = '{}' 
                                AND Staff.StaffID = ScheduledAt.StaffID
                                AND ScheduledAt.TheaterCode = Theaters.TheaterCode; '''.format(empName))
                print("##################################")
                # Print results to user
                for row in cur.fetchall():
                    code = row[0]
                    address = row[1]
                    sponsor = row[2]
                    print("Theater Code: {} ---> Address: {} ---> Sponsor: {}".format(code, address, sponsor))
                userInput = -1

            if userInput == 2: # Advanced Query 2
                cur.execute('''  SELECT Customers.Name, ConcessionStand.Name 
                                 FROM Customers, ConcessionPurchase, ConcessionStand
                                 WHERE Customers.MemberID = ConcessionPurchase.MemberID 
                                    AND ConcessionPurchase.ItemID = ConcessionStand.ItemID; ''')
                print("##################################")
                # Print results to user
                for row in cur.fetchall():
                    cust = row[0]
                    food = row[1]
                    print(f"Customer: {cust} ---> Food: {food}")
                userInput = -1

        if userInput == 0: # Go back to main_page()
            print("Returning to main page...\n\n")

# end of admin_page()

def about_page():
    print("\n\n##################################")
    print("This program is based on a movie theater database system.\n  Storing information relevant to movie theaters and their relationships.")

def member_portal(MemberID):
    userInput = -1
    while(userInput!=0):
        print("\n\n##################")
        print("Greetings JAR Member!!!")
        print("##################")
        print("Navigations: ")
        print("1.  See Profile")
        print("2.  Change Email or Password")
        print("3.  See Points")
        print("4.  See Purchased Tickets")
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
            print("Name: {}\nEmail: {}\nMemebrID: {}".format(name, email, MemberID))
        
        if userInput == 2: #  Change Email or Password
            cur.execute(''' SELECT Email, Password FROM Customers WHERE MemberID = '{}';'''.format(MemberID))
            output = cur.fetchall()
            email = output[0][0]
            password = output[0][1]
            print("Email: {}\nPassword: {}".format(email, password))

            email = input("New Email: ")
            password = input("New Password: ")
            for CHAR in INJECTIONCHARS:
                if ((CHAR in email) or (CHAR in password)):
                    print(f"Invalid character = {CHAR}\nReturning to Member Page...")
                    return
            cur.execute(''' UPDATE Customers SET email = '{}', password = '{}' WHERE MemberID = '{}'; '''.format(email, password, MemberID))
            print("###############################")
            print("Personal Information Updated!")

        if userInput == 3: #  See Points
            cur.execute(''' SELECT Points FROM Customers WHERE MemberID = '{}'; '''.format(MemberID))
            output = cur.fetchall()
            points = output[0][0]
            print("JAR Point Total: {}".format(points))

        if userInput == 4: #  See DISTINCTLY Purchased Tickets
            cur.execute(f''' SELECT DISTINCT Name, Duration, Director, Rated, Rating, is3D 
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
            # Select and print all movies 
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
            # Ask the user to input movie they would like to buy (int cast removes the need for injection check)
            userInput = int(input("Enter an ID to buy a ticket (or 0 to cancel): "))
            if userInput: # if user selected a movie ID, create movie data
                for movie in movies:
                    if int(movie[0]) == userInput:
                        movieName = movie[1] # movie name from previous cur.fetchall() stored in movies array
                ticketID = str(random.randint(9999999, 99999999))
                price = 6
                purchaser = MemberID # global memberID
                roomID = 2222
                seat = 9
                row = 'B'
                cur.execute(''' SELECT ShowingID FROM Showing WHERE MovieID = '{}'; '''.format(userInput))
                output = cur.fetchall()
                if output: # if userInput matches a movieID in the database, add ticket to database
                    Showing = output[0][0]
                    cur.execute(''' INSERT INTO Tickets(TicketID, Showing, Price, TicketPurchaser, RoomID, Seat, Row)
                                    VALUES ({}, {}, {}, {}, {}, {}, '{}');   
                                '''.format(ticketID, Showing, price, purchaser, roomID, seat, row))
                    conn.commit()
                    print("Congrats!!! Your ticket for {} has been purchased!!!".format(movieName))
                else:
                    print("MovieID does not exist. Returning to greeting page...")
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
