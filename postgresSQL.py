# import library for postgreSQL connection
import psycopg2

# connect to database server
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="database_design", port=5433)

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
        print("1.  Member Login <-- Under Construction")
        print("2.  Employee Login <-- Under Construction")
        print("3.  Admin Login")
        print("4.  About JAR <-- Under Construction")
        print("0.  Exit")

        # check user input
        userInput = int(input("Please select by entering one of digits 1-4: "))
        while(userInput < 0 or userInput > 4):
            print("---> Invalid selection <---")
            userInput = int(input("Please select by entering one of digits 1-4: "))

        # page transitions:
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
    # welcome interface
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

def about_page():
    pass


### Main ###
####################

# initiate program
main_page()

# close cursor and database connection
cur.close()
conn.close()

####################
### End Main ###
