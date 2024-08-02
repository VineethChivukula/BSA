CREATE TABLE bank_statement (
    statement_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    company_id INT NOT NULL,
    branch_id INT NOT NULL,
    statement_date DATE NOT NULL,
    statement_data VARCHAR(255) NOT NULL,
    PRIMARY KEY (statement_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (company_id) REFERENCES company(company_id),
    FOREIGN KEY (branch_id) REFERENCES branch(branch_id)
);