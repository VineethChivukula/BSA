CREATE TABLE transaction (
    transaction_id INT NOT NULL AUTO_INCREMENT,
    statement_id INT,
    date DATE,
    amount FLOAT,
    description VARCHAR(255),
    company_name VARCHAR(100),
    branch_id INT,
    PRIMARY KEY (transaction_id),
    FOREIGN KEY (statement_id) REFERENCES bank_statement(statement_id),
    FOREIGN KEY (branch_id) REFERENCES branch(branch_id)
);