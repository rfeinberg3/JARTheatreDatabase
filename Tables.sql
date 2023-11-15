CREATE TABLE IF NOT EXISTS Movies (
    MovieID VARCHAR(12) PRIMARY KEY,
    MovieName VARCHAR(50),
    Duration TIME,
    Director VARCHAR(50),
    Rated BOOLEAN,
    Rating INTEGER,
    is3D BOOLEAN
);

CREATE TABLE IF NOT EXISTS Theaters (
    TheaterCode VARCHAR(12) PRIMARY KEY,
    Address VARCHAR(100),
    Sponsor VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Rooms (
    TheaterCode VARCHAR(12) REFERENCES Theaters ON DELETE CASCADE,
    RoomID INTEGER PRIMARY KEY,
    isXD BOOLEAN,
    Capacity INTEGER
);

CREATE TABLE IF NOT EXISTS At (
    MovieID VARCHAR(12) REFERENCES Movies NOT NULL,
    TheaterCode VARCHAR(12) REFERENCES Theaters NOT NULL
);

CREATE TABLE IF NOT EXISTS Showing (
    ShowingID VARCHAR(10) PRIMARY KEY,
    MovieID VARCHAR(12) REFERENCES Movies NOT NULL,
    MovieName VARCHAR(50),
    Date DATE,
    StartTime TIME,
    TheaterCode VARCHAR(12) REFERENCES Theaters NOT NULL,
    RoomID INTEGER REFERENCES Rooms NOT NULL
);

CREATE TABLE IF NOT EXISTS Customers (
	MemberID CHAR(10) PRIMARY KEY, 
	Password VARCHAR(50) NOT NULL, 
	Points INTEGER, 
	Name VARCHAR(50), 
	Email VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Tickets (
	TicketID CHAR(8) PRIMARY KEY, 
	Showing VARCHAR(10) REFERENCES Showing NOT NULL, 
	Price NUMERIC(9, 2), 
	TicketPurchaser CHAR(10) REFERENCES Customers, 
	RoomID VARCHAR(12), 
	Seat CHAR(2), 
	Row CHAR(2)
);

CREATE TABLE IF NOT EXISTS Staff (
	StaffID CHAR(10) PRIMARY KEY, 
	Name VARCHAR(50), 
	Email VARCHAR(50), 
	PhoneNumber INTEGER
);

CREATE TABLE IF NOT EXISTS ConcessionStand (
	ItemID CHAR(6) PRIMARY KEY, 
	Name VARCHAR(50), 
	Price NUMERIC(9,2), 
	Quantity INTEGER
);

CREATE TABLE IF NOT EXISTS ConcessionPurchase (
	Receipt INTEGER PRIMARY KEY, 
	MemberID CHAR(10) REFERENCES Customers, 
	ItemID CHAR(6) REFERENCES ConcessionStand
);

CREATE TABLE IF NOT EXISTS ScheduledAt (
	StaffID CHAR(10) REFERENCES Staff, 
	TheaterCode VARCHAR(12) REFERENCES Theaters
);