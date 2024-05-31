--scripts to create database with unique id

CREATE TABLE IF NOT EXISTS your_database_name.unique_id(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	UNIQUE key (id)
	) ENGINE=InnoDB DEFAULT=utf8mb4
