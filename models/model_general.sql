CREATE TABLE users (
    id int NOT NULL,
    first_name varchar(10),
    age int,
    email varchar(20),
    password varchar(200),
    PRIMARY KEY (id)
);

CREATE TABLE messages (
    id int NOT NULL,
    message_day varchar(255),
    message_img varchar(255),
    date_day_publish DATE,
    PRIMARY KEY (id)
);

ALTER TABLE users MODIFY COLUMN id int NOT NULL AUTO_INCREMENT;
ALTER TABLE messages MODIFY COLUMN id int NOT NULL AUTO_INCREMENT;