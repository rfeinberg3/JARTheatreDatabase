# Jar Movies Database System

## Overview

The Jar Movies database system is designed to manage information relevant to a movie theater, including the relationships between various entities. The system offers different privileges for Members and Staff, providing distinct views and access levels for each type of user. To ensure database security, we implemented invalid character detection to prevent SQL injection attacks.

## Design

- **Database:** PostgreSQL
- **Interface:** Python

The system uses the Psycopg2 library for communication between the Python code and the PostgreSQL database.

### Connection Example
```python
import psycopg2

# Connect to database server
conn = psycopg2.connect(host="localhost", dbname="jarMovies", user="postgres", password="database_design", port=5433)

# Create cursor to database
cur = conn.cursor()
```

### Table Creation and Value Insertion
Table creation and value insertion are handled by running `Tables.sql` and `Insert.sql` respectively.
```python
# Initiate tables in database if they don't exist
cur.execute(open("/path/to/Tables.sql", "r").read())
conn.commit()

# Insert into or update values in database
cur.execute(open("/path/to/Inserts.sql", "r").read())
conn.commit()
```

### Key Changes in Database Design
- **Showing Table:** Added `ShowingID` as the primary key instead of using `movieID` because a movie can have different showings (e.g., different rooms and times).
- **ConcessionPurchase Table:** Added `Receipt` as the primary key instead of using two foreign keys.

### Interface Design
The coding style is functional, with each page of the interface represented by a function. Each function leads to a “deeper” page within the program or returns to the calling function.

#### Main Page Function Example
```python
def main_page():
    userInput = -1
    while(userInput != 0):
        print("\n\n##################################")
        print("Welcome to JAR, where movies are.")
        print("##################################")
        print("Navigations: ")
        print("1. Member Login")
        print("2. Admin Page")
        print("3. About JAR")
        print("0. Exit")

        userInput = int(input("Please select by entering one of digits 0-3: "))
        while(userInput < 0 or userInput > 3):
            print("---> Invalid selection <---")
            userInput = int(input("Please select by entering one of digits 0-3: "))

        # Page transitions
        if userInput == 1:
            member_login()
        if userInput == 2:
            admin_page()
        if userInput == 3:
            about_page()
        if userInput == 0:
            print("Exiting program... Goodbye :)")
```

## Security Measures
The system checks for SQL injection attacks by validating user inputs against a pre-generated list of invalid characters.

```python
INJECTIONCHARS = [',', '\'', '-', '#', ';']

def validate_input(name, email, password):
    for CHAR in INJECTIONCHARS:
        if CHAR in name or CHAR in email or CHAR in password:
            print(f"Invalid character = {CHAR}\nReturning to Main Page...")
            return False
    return True
```

## Main Functionality
The program uses a command-line interface. Upon loading, the user sees the main page with navigations to various functionalities.

### Member Portal Functions
1. Check user's name, email, and MemberID.
2. Change email and/or password.
3. Check user points.
4. View all tickets purchased by the user.
5. Browse and purchase tickets for movies being shown.

### Admin Page
Provides a command-line interface for direct access to the database and its functionalities, allowing administrators to execute SQL statements.

## Conclusion
The Jar Movies database system offers a secure and efficient way to manage movie theater data, with distinct user privileges and robust security measures against SQL injection attacks. The functional coding style ensures a clear and maintainable interface design.