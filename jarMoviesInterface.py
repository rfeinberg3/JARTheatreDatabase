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
        print("3.  See Showtimes")
        print("4.  About JAR <-- Under Construction")
        print("0.  Exit")

        # check user input
        userInput = int(input("Please select by entering one of digits 0-4: "))
        while(userInput < 0 or userInput > 4):
            print("---> Invalid selection <---")
            userInput = int(input("Please select by entering one of digits 0-4: "))

        # page transitions:
        if userInput == 1:
            member_login()
        if userInput == 2:
            admin_page()
        if userInput == 3:
            showtime_page()
        if userInput == 4:
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
    password = input("Enter the admin password: ")
    if password != "jar":
        print("incorrect password")
        return
    # welcome interface
    userInput = -1
    while(userInput!=0):
        print("\n\n##################################")
        print("Administrative page. All funtionality available")
        print("Navigations: ")
        print("1.  INSERT")
        print("2.  SELECT")
        print("3.  DELETE")
        print("4.  Employee Information")
        print("5.  Customer Information")
        print("6.  Theater Information")
        print("0.  Back")

        # make a selection
        userInput = int(input("Selection: "))
        while(userInput < 0 or userInput > 3):
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
        if userInput == 0: # Exit 
            print("Returning to main page...\n\n")
# end of admin_page()

def showtime_page():
    pass

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
        print("0.  Logout")
        # check user input
        userInput = int(input("Please select by entering one of digits 0-3: "))
        while(userInput < 0 or userInput > 3):
            print("---> Invalid selection <---")
            userInput = int(input("Please select by entering one of digits 0-3: "))

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
