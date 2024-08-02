# Bank Statement Aggregator

## Project Overview

The Bank Statement Aggregator is a comprehensive system designed to manage and process bank statements for multiple companies and their branches. This project includes functionalities for generating, uploading, downloading, and updating bank statements, as well as aggregating data for analysis.

## Prerequisites

- Python 3.x
- MySQL
- AWS Account with S3 Bucket
- Required Python packages (listed in `requirements.txt`)

## Project Structure

```
BSA
├── .venv
├── app
|   ├── controllers
|   |   ├── __init__.py 
│   │   ├── branch_controller.py
│   │   ├── company_controller.py
│   │   ├── statement_controller.py
│   │   └── user_controller.py
│   ├── models
│   │   ├── bank_statement.py
│   │   ├── branch.py
│   │   ├── company.py
│   │   ├── transaction.py
│   │   └── user.py
│   ├── repositories
│   │   ├── bank_statement_repository.py
│   │   ├── branch_repository.py
│   │   ├── company_repository.py
│   │   ├── transaction_repository.py
│   │   └── user_repository.py
│   ├── services
│   │   ├── aws_service.py
│   │   ├── bank_statement_service.py
│   │   ├── branch_service.py
|   |   ├── company_service.py
│   │   └── user_service.py
│   ├── utils
│   │   ├── db.py
│   │   ├── parser.py
│   │   └── s3.py
│   ├── __init__.py 
│   └── config.py 
├── migrations
│   ├── 001_create_company_table.sql
│   ├── 002_create_branch_table.sql
│   ├── 003_create_user_table.sql
│   ├── 004_create_bank_statement_table.sql
│   └── 005_create_transaction_table.sql
├── scripts
│   ├── aggregate_statements.py
│   ├── download_from_s3.py
│   ├── generate_transactions.py
│   ├── update_database.py
│   └── upload_to_s3.py
├── .env
├── .gitignore
├── .LICENSE
├── main.py
├── README.md
└── requirements.txt
```

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/VineethChivukula/BSA.git
   cd BSA
   ```

2. **Set Up Virtual Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database**

   ```bash
   cd migrations
   mysql -u your_username -p
   your_password
   create database bsa;   
   source 001_create_company_table.sql
   source 002_create_branch_table.sql
   source 003_create_user_table.sql
   source 004_create_bank_statement_table.sql
   source 005_create_transaction_table.sql
   ```

5. **Configure AWS S3**

   Ensure you have AWS credentials set up with access to the S3 bucket.

## Usage

**Run The Application**

   This script creates random transactions for designated companies and branches. It then uploads the generated CSV files to a specified S3 bucket, downloads the CSV files from the S3 bucket to the local system, reads the downloaded CSV files, updates the transactions in the database, aggregates transactions for the selected company, and saves the aggregated data into a CSV file.

   ```bash
   python main.py
   ```

## Scripts Explanation

- **generate_transactions.py**: 
This script defines a process for generating random transactions for multiple companies and their branches, saving these transactions to CSV files. Here are the details:

   1. **generate_random_transactions**:
      - Generates a specified number of random transactions for a given company branch.
      - Each transaction includes a transaction ID, statement ID, date, amount, description, company name, branch name, branch ID, bank name, user ID, and company ID.
      - Transaction dates are randomly distributed within the given month and year.
      - Returns a list of transactions.

   2. **save_transactions_to_csv**:
      - Saves the list of transactions to a CSV file.
      - Creates a directory named `gen_data` if it doesn't already exist.
      - Writes the transactions to a CSV file with a specified filename in the `gen_data` directory.
      - Prints an error message if there is an issue writing to the file.

   3. **get_month_year_selection**:
      - Prompts the user to select a month and year for which the transactions should be generated.
      - Provides a list of months and years to choose from.
      - Validates the user input for month and year selection.
      - Returns the selected month and year.

   4. **generate**:
      - Defines a dictionary of companies, each with multiple branches, bank details, user IDs, and company IDs.
      - Calls `get_month_year_selection` to get the user's desired month and year for transaction generation.
      - If valid month and year are selected, iterates over each company and its branches.
      - Generates random transactions for each branch using `generate_random_transactions`.
      - Saves the generated transactions to a CSV file using `save_transactions_to_csv`.
      - Prints a confirmation message for each generated statement.

- **upload_to_s3.py**:
This script defines a function to upload CSV files from a local directory to an S3 bucket using a client from a utility module. Here are the details:

   1. **upload**:
      - Ensures the existence of the `gen_data` directory, creating it if necessary.
      - Traverses the `gen_data` directory to find all files.
      - For each file found with a `.csv` extension:
         - Constructs the full file path.
         - Attempts to upload the file to S3 using the `S3Client.upload_file` method.
         - Prints a success message with the S3 URL if the upload is successful.
         - Prints an error message if there is an issue uploading the file.
      - Prints a confirmation message once all files are uploaded.
      - Prints an error message if there is an issue creating the directory or any other unexpected error occurs during the process.

- **download_from_s3.py**: 
The code snippet defines functions for listing and downloading CSV files from an S3 bucket based on the specified year and month. Here are the details:

   1. **list_s3_files(bucket, year, month)**:
      - This function initializes an S3 client using `boto3` with AWS credentials from the configuration file.
      - It lists all objects in the specified S3 bucket.
      - Filters the listed objects to only include those ending with `.csv` and containing the specified year and month in their filename.
      - Returns a list of filtered keys.

   2. **download()**:
      - Prompts the user to input the year and month for which they want to download statements.
      - Calls `list_s3_files` with the specified year and month to retrieve the relevant file keys from the S3 bucket.
      - If matching keys are found, it prepares the data dictionary with the keys and calls `S3Client.download_files` to download the files.
      - Prints a message confirming that the statements have been downloaded.
      - Saves the specified year and month to a temporary configuration file named `temp_config.txt`.
      - If no matching statements are found in the S3 bucket, it prints an appropriate message and exits the program with an error code.
      - Any exceptions that occur during the process are caught and printed.

- **update_database.py**: 
This script outlines functions for reading CSV files, creating or retrieving database entities, and saving transactions to the database. Here are the details:

   1. **read_csv(file_path)**:
      - Reads transactions from a CSV file located at `file_path`.
      - Returns a list of transactions read from the file.
      - Prints an error message if the file cannot be read.

   2. **get_or_create_company(company_name)**:
      - Retrieves a company by its name from the database.
      - If the company does not exist, it creates a new company entry in the database.
      - Returns the company object.
      - Prints an error message if there is an issue creating or retrieving the company.

   3. **get_or_create_branch(branch_name, company_name, bank_name)**:
      - Retrieves the associated company using `get_or_create_company`.
      - Retrieves a branch by its name and company ID from the database.
      - If the branch does not exist, it creates a new branch entry in the database.
      - Returns the branch object.
      - Prints an error message if there is an issue creating or retrieving the branch.

   4. **save_user(transaction)**:
      - Retrieves the associated company using `get_or_create_company`.
      - Searches for a user by their email in the database.
      - If the user does not exist, it encrypts the email and password, creates a new user entry in the database, and assigns them to the company.
      - Returns the user ID.
      - Prints an error message if there is an issue saving the user.

   5. **save_bank_statement(transaction, user_id)**:
      - Retrieves the associated company using `get_or_create_company`.
      - Retrieves the associated branch using `get_or_create_branch`.
      - Creates a new bank statement entry in the database with the current date and a reference to the transaction CSV file stored in S3.
      - Returns the statement ID.
      - Prints an error message if there is an issue saving the bank statement.

   6. **save_transactions_to_db(transactions)**:
      - Iterates through the list of transactions.
      - For each transaction, it saves the user using `save_user`.
      - If the user is successfully saved, it saves the bank statement using `save_bank_statement`.
      - If the bank statement is successfully saved, it saves the transaction details in the database.
      - Commits the changes to the database.
      - Rolls back the transaction and prints an error message if there is an issue saving the transactions.

   7. **update()**:
      - Traverses the `down_data` directory, searching for CSV files.
      - For each CSV file found, it reads the transactions using `read_csv`.
      - Saves the transactions to the database using `save_transactions_to_db`.
      - Prints a confirmation message upon successful saving.
      - Prints an error message if there is an issue updating the database.

- **aggregate_statements.py**: 
This script provides functions for fetching, aggregating, and saving transaction data for a specified company, year, and month. Here are the details:

   1. **get_transactions_for_company(company_name, year, month)**:
      - Queries the database to fetch transactions for the specified company, year, and month.
      - Joins the `Transaction` and `Branch` tables to retrieve branch details along with each transaction.
      - Filters transactions based on the company name and the specified date range (the specified month of the specified year).
      - Returns a list of transactions with associated branch details.

   2. **aggregate_and_save(transactions, company_name)**:
      - Aggregates the total debits and credits from the transactions.
      - Creates a directory named `aggr_data` if it doesn't already exist.
      - Writes the transactions to a CSV file named `{company_name}_aggregated.csv` within the `aggr_data` directory.
      - Includes headers for transaction details and writes each transaction along with branch details to the CSV.
      - Adds two additional rows to the CSV for total debits and total credits.
      - Prints the file path of the saved aggregated data, along with the total debits and credits.

   3. **aggregate()**:
      - Reads the year and month from a temporary configuration file (`temp_config.txt`).
      - Prompts the user to select a company from a predefined list of options (Apple_India, Apple_US, Google_India, Google_US).
      - Based on the user's selection, retrieves the transactions for the specified company, year, and month using `get_transactions_for_company`.
      - Calls `aggregate_and_save` to aggregate and save the transactions to a CSV file.
      - Prints an error message if the temporary configuration file is not found or if an invalid company choice is made.

## Contributors

- **[Sai Kumar Gouru](https://www.linkedin.com/in/sai-kumar-gouru-972623a8/)** - Designed the problem statement
- **[Vineeth Chivukula](https://www.linkedin.com/in/vineethchivukula)** - Code and logic


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- I would like to extend my sincere gratitude to [Hema](https://www.linkedin.com/in/hemaannaluru/) and [Srujana](https://www.linkedin.com/in/srujanavattamwar/) for their invaluable support. Their patience and belief in my abilities were instrumental in the successful completion of this work.