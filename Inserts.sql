INSERT INTO Movies(MovieID, Name, Duration, Director, Rated, Rating, is3D)
	VALUES
	(123456789101, 'The Hunger Games', '2:38', 'Francis Lawrence', 'true', 7, 'false'),
	(111111111111, 'Wish', '1:35', 'Fawn Veerasunthorn', 'false', -1, 'false'),
	(222222222222, 'Tiger 3', '2:37', 'Maneesh Sharma', 'true', 8, 'true'),
	(333333333333, 'Made Up Movie', '0:59', 'Ryan Feinberg', 't', 10, 't');


INSERT INTO Theaters(TheaterCode, Address, Sponsor) 
	VALUES 
	(1111, '123 Movie Ln', 'AMC'),
	(2222, '987 Theater Blvd', 'Regal Theaters'),
	(3333, '567 Business Dr', 'Local Theater');

INSERT INTO Rooms(RoomID, TheaterCode, isXD, Capacity) 
	VALUES 
	(1, 1111, 'false', 80),
	(2, 1111, 'false', 75),
	(3, 1111, 'true', 100),
	(4, 1111, 'false', 85),
	(5, 1111, 'true', 120);


INSERT INTO At(MovieID, TheaterCode) 
	VALUES
	(123456789101, 1111),
	(111111111111, 2222),
	(222222222222, 3333),
	(333333333333, 1111);

INSERT INTO Showing(ShowingID, MovieID, MovieName, Date, StartTime, TheaterCode, RoomID)
	VALUES
	(123456789, 123456789101, 'The Hunger Games', '01-01-2023', '17:00:00', 1111, 1),
	(234567890, 111111111111, 'Wish', '01-01-2023', '13:30:00', 1111, 2),
	(564789123, 222222222222, 'Tiger 3', '01-01-2023', '16:00:00', 1111, 3),
	(456789412, 333333333333, 'Made Up Movie', '01-01-2023', '20:30:00', 1111, 5),
	(456879122, 123456789101, 'The Hunger Games', '01-01-2023', '18:00:00', 2222, 1),
	(546897123, 111111111111, 'Wish', '01-01-2023', '14:00:00', 2222, 3),
	(984156448, 222222222222, 'Tiger 3', '01-01-2023', '15:30:00', 2222, 2),
	(456897412, 333333333333, 'Made Up Movie', '01-01-2023', '15:00:00', 3333, 4),
	(456789121, 123456789101, 'The Hunger Games', '01-01-2023', '17:30:00', 3333, 1),
	(647861234, 222222222222, 'Tiger 3', '01-01-2023', '19:00:00', 3333, 2);

INSERT INTO Customers(MemberID, Password, Points, Name, Email)
	VALUES
	('0123456789', crypt('ExpOfPassword?', gen_salt('md5')), 0, 'Jonh Doe', 'joedoe@yahoo.com'),
	('0795246801', crypt('oU3.&B=\a%S!', gen_salt('md5')), 80, 'Genia Bendix', 'gbendix0@yelp.com'),
	('2419646792', crypt('cU6#JS!?GT&', gen_salt('md5')), 34, 'Arlyne McAvey', 'amcavey1@gmail.com'),
	('8232602008', crypt('yO6#VMC378\{Z', gen_salt('md5')), 90, 'Tate Conrart', 'tconrart4@icloud.com'),
	('1093764048', crypt('bH3#Ry.&3($p(3', gen_salt('md5')), 65, 'Stepha Bromby', 'sbromby9@gmail.com');

INSERT INTO Tickets(TicketID, Showing, Price, TicketPurchaser, RoomID, Seat, Row)
	VALUES
	('01234567', '234567890', 9.99, '0123456789', '2', 1, 'A'),
	('01234568', '234567890', 9.99, '0123456789', '2', 2, 'A'),
	('01234569', '234567890', 9.99, '0123456789', '2', 3, 'A'),
	('01234570', '234567890', 9.99, '0123456789', '2', 4, 'A'),
	('01234571', '234567890', 9.99, '0123456789', '2', 5, 'A');

INSERT INTO Staff(StaffID, Name, Email, PhoneNumber)
	VALUES
	('0101010100', 'Lewis Sheeran', 'lsheeran3@gamil.com', 1356305033),
	('0245843220', 'Abby Jonhson', 'abjohn@yahoo.com', 1197675399),
	('0123456770', 'Clement	Matthew', 'cmatthew@yelp.com', 1874565024);

INSERT INTO ConcessionStand(ItemID, Name, Price, Quantity)
	VALUES
	('000000', 'Small Popcorn', 7.09, 60),
	('000001', 'Medium Popcorn', 8.09, 50),
	('000002', 'Large Popcorn', 9.09, 55),
	('252710', 'Candy', 3.99, 120),
	('936512', 'Nachos', 7.59, 600),
	('786210', 'Small Soft Drink', 5.09, 100),
	('786211', 'Medium Soft Drink', 5.79, 100),
	('786212', 'Large Soft Drink', 6.29, 90);

INSERT INTO ConcessionPurchase(Receipt, MemberID, ItemID)
	VALUES
	(100, '0795246801', '000000');

INSERT INTO ScheduledAt(StaffID, TheaterCode)
	VALUES
	('0101010100', '1111'),
	('0245843220', '2222'),
	('0123456770', '3333');
