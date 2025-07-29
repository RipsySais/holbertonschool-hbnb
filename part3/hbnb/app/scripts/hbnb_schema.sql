DROP TABLE IF EXISTS `place_amenity`;
DROP TABLE IF EXISTS `review`;
DROP TABLE IF EXISTS `place`;
DROP TABLE IF EXISTS `amenity`;
DROP TABLE IF EXISTS `user`;

-- SQL table for User
CREATE TABLE IF NOT EXISTS `user`(
	id CHAR(36) PRIMARY KEY,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	email VARCHAR(255) UNIQUE NOT NULL,
	password VARCHAR(255) NOT NULL,
	is_admin BOOLEAN DEFAULT FALSE
	);

-- SQL table for Place
CREATE TABLE IF NOT EXISTS `place`(
	id CHAR(36) PRIMARY KEY,
	title VARCHAR(255) NOT NULL,
	description TEXT,
	price DECIMAL(10, 2),
	latitude FLOAT,
	longitude FLOAT,
	owner_id CHAR(36),
	FOREIGN KEY (owner_id) REFERENCES `user`(id) ON DELETE CASCADE
	);

-- SQL table for Review
CREATE TABLE IF NOT EXISTS `review`(
	id CHAR(36) PRIMARY KEY,
	text TEXT,
 	rating INT CHECK (rating BETWEEN 1 AND 5),
 	user_id CHAR(36),
 	place_id CHAR(36),
 	UNIQUE(user_id, place_id),
 	FOREIGN KEY (user_id) REFERENCES `user`(id) ON DELETE CASCADE,
 	FOREIGN KEY (place_id) REFERENCES `place`(id) ON DELETE CASCADE
	);

-- SQL table for Amenity
CREATE TABLE IF NOT EXISTS `amenity`(
 	id CHAR(36) PRIMARY KEY,
 	name VARCHAR(255) UNIQUE NOT NULL
	);

CREATE TABLE IF NOT EXISTS `place_amenity`(
 	place_id CHAR(36),
 	amenity_id CHAR(36),
 	PRIMARY KEY (place_id, amenity_id),
 	FOREIGN KEY (place_id) REFERENCES `place`(id) ON DELETE CASCADE,
 	FOREIGN KEY (amenity_id) REFERENCES `amenity`(id) ON DELETE CASCADE
	);
