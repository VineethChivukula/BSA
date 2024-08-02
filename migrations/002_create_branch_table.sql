CREATE TABLE branch (
    branch_id INT NOT NULL AUTO_INCREMENT,
    branch_name VARCHAR(100) NOT NULL,
    company_id INT,
    bank_name VARCHAR(100),
    PRIMARY KEY (branch_id),
    FOREIGN KEY (company_id) REFERENCES company(company_id)
);