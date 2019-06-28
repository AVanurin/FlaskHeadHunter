PRAGMA foreign_keys=on;

DROP IF EXISTS TABLE users;

CREATE TABLE users (
id INT PRIMARY KEY AUTO_INCREMENT,
login VARCHAR(25) UNIQUE,
email VARCHAR(20) UNIQUE,
password VARCHAR(20)
);

DROP IF EXISTS TABLE profiles;

CREATE TABLE profiles (
id INT PRIMARY KEY,
fname VARCHAR(20),
lname VARCHAR(20),
age INT,
sex VARCHAR(10),
job VARCHAR(255),
FOREIGN KEY (id) REFERENCES users(id)
);

DROP IF EXISTS TABLE summaries;

CREATE TABLE summaries (
id INT PRIMARY KEY,
u_id INT,
job_title VARCHAR(50),
info TEXT(),
FOREIGN KEY (u_id) REFERENCES users(id)
);





