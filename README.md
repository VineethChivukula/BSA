# Bank Statement Aggregator

## Project Overview

The Bank Statement Aggregator is a comprehensive system designed to manage and process bank statements for multiple companies and their branches. This project includes functionalities for generating, uploading, downloading, and updating bank statements, as well as aggregating data for analysis.

## Features

- **Generate Random Transactions**: Generates random transactions for multiple companies and branches.
- **Upload Statements to S3**: Uploads the generated CSV files containing transactions to an S3 bucket.
- **Download Statements from S3**: Downloads the CSV files from the S3 bucket to the local system.
- **Update Database**: Inserts the downloaded transactions into the database.
- **Aggregate Data**: Aggregates transactions for selected companies and saves the aggregated data into a CSV file.

## Prerequisites

- Python 3.x
- MySQL
- AWS Account with S3 Bucket
- Required Python packages (listed in `requirements.txt`)

## Project Structure

```
BSA
├── app
|   ├── controllers
|   |   ├── __init__.py 
│   │   ├── branch_controller.py
│   │   ├── company_controller.py
│   │   ├── statement_controller.py
│   │   └── user_controller.py
│   ├── models
│   │   ├── user.py
│   │   ├── company.py
│   │   ├── branch.py
│   │   ├── bank_statement.py
│   │   └── transaction.py
│   ├── repositories
│   │   ├── user_repository.py
│   │   ├── company_repository.py
│   │   ├── branch_repository.py
│   │   ├── bank_statement_repository.py
│   │   └── transaction_repository.py
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
│   └── __init__.py 
├── migrations
│   ├── 001_create_company_table.sql
│   ├── 002_create_branch_table.sql
│   ├── 003_create_user_table.sql
│   ├── 004_create_bank_statement_table.sql
│   └── 005_create_transaction_table.sql
├── scripts
│   ├── generate_transactions.py
│   ├── upload_to_s3.py
│   ├── download_from_s3.py
│   ├── update_database.py
│   └── aggregate_statements.py
├── .venv
├── requirements.txt
├── README.md
└── main.py
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

   - Create the necessary MySQL database and tables using the `create_db_schema.sql` script provided in the `scripts` directory.

5. **Configure AWS S3**

   - Ensure you have AWS credentials set up with access to the S3 bucket.

6. **Run the Application**

   ```bash
   python main.py
   ```

## Usage

**Run The Application**

   This script creates random transactions for designated companies and branches. It then uploads the generated CSV files to a specified S3 bucket, downloads the CSV files from the S3 bucket to the local system, reads the downloaded CSV files, updates the transactions in the database, aggregates transactions for the selected company, and saves the aggregated data into a CSV file.

   ```bash
   python main.py
   ```

## Contributors

- **[Sai]** - Problem Statement
- **[Vineeth]** - Code and Logic


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to everyone who contributed to the development of this project.
```