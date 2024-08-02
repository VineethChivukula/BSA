CREATE TABLE user (
    user_id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    company_id INT,
    PRIMARY KEY (user_id),
    FOREIGN KEY (company_id) REFERENCES company(company_id)
);