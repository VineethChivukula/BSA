from datetime import datetime
import os
from app.repositories.branch_repository import BranchRepository
from app.repositories.company_repository import CompanyRepository  # Ensure this import is correct
from app.utils.s3 import S3Client
from app.repositories.bank_statement_repository import BankStatementRepository
from app.repositories.transaction_repository import TransactionRepository
from app.utils.parser import Parser
from scripts.generate_transactions import generate_random_transactions


class BankStatementService:
    @staticmethod
    def generate_statement(data):
        try:
            # Generate CSV statement file
            statement_file_path = Parser.generate_csv(data)
            return statement_file_path
        except Exception as e:
            raise Exception(f"Error generating statement: {str(e)}")

    @staticmethod
    def upload_statement(data):
        try:
            file_path = data['file_path']
            # Upload file to S3 and get the URL
            s3_url = S3Client.upload_file(file_path)
            # Ensure statement_data is included
            data['statement_data'] = s3_url
            # Save statement data to the repository
            BankStatementRepository.save_statement(data, s3_url)
            # Get the statement ID
            statement_id = BankStatementRepository.get_statement_id(data)
            if statement_id:
                # Parse transactions from the CSV file
                transactions = Parser.parse_csv(file_path)
                # Add transactions to the statement
                TransactionRepository.add_transactions(
                    transactions, statement_id, data['branch_id'])
            else:
                raise Exception("Failed to retrieve statement ID")
        except Exception as e:
            raise Exception(f"Error uploading statement: {str(e)}")

    @staticmethod
    def upload_statements(user_id, company_records):
        os.makedirs('generated_data', exist_ok=True)
        for company, details in company_records.items():
            company_id = details['company_id']
            for branch_name in details['branches']:
                branch = BranchRepository.get_branch_by_name_and_company(
                    branch_name, company_id)
                if not branch:
                    print(f"Branch {branch_name} not found for company {company}")
                    continue
                
                data = generate_random_transactions(company, branch_name)
                print(f"Statement generated for {company} - {branch_name}")
                try:
                    statement = BankStatementService.generate_statement(data)

                    upload_data = {
                        "user_id": user_id,
                        "company_id": company_id,
                        "branch_id": branch.branch_id,
                        "statement_date": datetime.now().strftime('%Y-%m-%d'),
                        "file_path": statement
                    }
                    BankStatementService.upload_statement(upload_data)
                    print(f"Statement uploaded successfully for {company} - {branch_name}")
                except Exception as e:
                    print(f"Error: {str(e)}")