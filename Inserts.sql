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

INSERT INTO Rooms(TheaterCode, RoomID, isXD, Capacity) 
	VALUES 
	(1111, 1, 'false', 80),
	(1111, 2, 'false', 75),
	(1111, 3, 'true', 100),
	(1111, 4, 'false', 85),
	(1111, 5, 'true', 120),
	(2222, 1, 'false', 80),
	(2222, 2, 'true', 110),
	(2222, 3, 'false', 65),
	(2222, 4, 'true', 100),
	(3333, 1, 'false', 40),
	(3333, 2, 'true', 50);

INSERT INTO At(MovieID, TheaterCode) 
	VALUES
	(123456789101, 1111),
	(111111111111, 2222),
	(222222222222, 3333),
	(333333333333, 1111);

INSERT INTO Showing(ShowingID, MovieID, MovieName, Date, StartTime, TheaterCode, RoomID)
	VALUES
	(123456789, 123456789101, 'The Hunger Games', '01-01-2023', '01-01-2023 17:00', 1111, 1),
	(234567890, 111111111111, 'Wish', '01-01-2023', '01-01-2023 13:30', 1111, 2),
	(564789123, 222222222222, 'Tiger 3', '01-01-2023', '01-01-2023 16:00', 1111, 3),
	(456789412, 333333333333, 'Made Up Movie', '01-01-2023', '01-01-2023 20:30', 5),
	(456879122, 123456789101, 'The Hunger Games', '01-01-2023', '01-01-2023 18:00', 2222, 1),
	(546897123, 111111111111, 'Wish', '01-01-2023', '01-01-2023 14:00', 2222, 3),
	(984156448, 222222222222, 'Tiger 3', '01-01-2023', '01-01-2023 15:30', 2222, 2),
	(456897412, 333333333333, 'Made Up Movie', '01-01-2023', '01-01-2023 15:00', 4),
	(456789121, 123456789101, 'The Hunger Games', '01-01-2023', '01-01-2023 17:30', 3333, 1),
	(647861234, 222222222222, 'Tiger 3', '01-01-2023', '01-01-2023 19:00', 3333, 2);

INSERT INTO Customers(MemberID, Password, Points, Name, Email)
	VALUES
	('0123456789', 'ExpOfPassword?', 0, 'Jonh Doe', 'joedoe@yahoo.com'),
	('0795246801', 'oU3.&B=\a%S!', 80, 'Genia Bendix', 'gbendix0@yelp.com'), 
	('2419646792', 'cU6#JS!?GT&', 34, 'Arlyne McAvey', 'amcavey1@gmail.com'),
	('8232602008', 'yO6#VMC378\{Z', 90, 'Tate Conrart', 'tconrart4@icloud.com')
	('1093764048', 'bH3#Ry.&3($p(3', 65, 'Stepha Bromby', 'sbromby9@gmail.com');

INSERT INTO Tickets(TicketID, Showing, Price, TicketPurchaser, RoomID, Seat, Row)
	VALUES
	();

INSERT INTO Staff(StaffID, Name, Email, PhoneNumber)
	VALUES
	();

INSERT INTO ConcessionStand(ItemID, Name, Price, Quantity)
	VALUES
	();

INSERT INTO ConcessionPurchase(Receipt, MemberID, ItemID)
	VALUES
	();

INSERT INTO ScheduledAt(StaffID, TheaterCode)
	VALUES
	();
