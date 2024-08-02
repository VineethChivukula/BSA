CREATE TABLE company (
    company_id INT NOT NULL AUTO_INCREMENT,
    company_name VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY (company_id)
);