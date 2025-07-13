-- Insertion of admin user
INSERT INTO `user` (id, first_name, last_name, email, password, is_admin)
VALUES (
	'36c9050e-ddd3-4c3b-9731-9f487208bbc1',
	'Admin',
	'HBnB',
	'admin@hbnb.io',
	'$2b$12$ByvHh4Z.y/t.PTDpcBdE.eWqyg2qxLZAhS8ZuXJy3UFIkdymTJ27C', -- bcrypt hash of "admin1234"
	TRUE
	);

INSERT INTO amenity (id, name) VALUES ('52318685-679c-4ad1-bc59-db782a317a2e', 'WIFI');
INSERT INTO amenity (id, name) VALUES ('57c80eed-5cc0-4d6b-ba86-cddeac8ddb92', 'Swimming Pool');
INSERT INTO amenity (id, name) VALUES ('8a6d2319-06a6-4d21-a055-0687f69061b7', 'Air Conditioning');
