import csv
import os

class Parser:
    @staticmethod
    def generate_csv(data):
        os.makedirs('generated_data', exist_ok=True)
        file_name = f"{data['company_name']}_{data['branch_name']}_{data['date'].replace('-', '')}.csv"
        file_path = os.path.join('generated_data', file_name)
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['date', 'amount', 'description', 'company_name'])
            for transaction in data['transactions']:
                writer.writerow([
                    transaction['date'],
                    transaction['amount'],
                    transaction['description'],
                    data['company_name']
                ])
        return file_path

    @staticmethod
    def parse_csv(file_path):
        transactions = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append({
                    'date': row['date'],
                    'amount': float(row['amount']),
                    'description': row['description'],
                    'company_name': row['company_name']
                })
        return transactions
