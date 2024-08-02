import logging
from app.models.transaction import Transaction
from app.utils.db import db


class TransactionRepository:
    @staticmethod
    def add_transactions(transactions, statement_id, branch_id):
        for transaction in transactions:
            # Add the statement_id to each transaction
            transaction['statement_id'] = statement_id
            # Add the branch_id to each transaction
            transaction['branch_id'] = branch_id
            # Create a new Transaction object with the modified transaction data
            new_transaction = Transaction(**transaction)
            # Add the new transaction to the database session
            db.session.add(new_transaction)
        # Commit the changes to the database
        db.session.commit()
        logging.info("Transactions added successfully")

    @staticmethod
    def aggregate_transactions(transactions):
        # Calculate the total debits by summing the amounts of transactions with negative amounts
        total_debits = sum(t['amount']
                           for t in transactions if t['amount'] < 0)

        # Calculate the total credits by summing the amounts of transactions with positive amounts
        total_credits = sum(t['amount']
                            for t in transactions if t['amount'] > 0)

        # Return a dictionary with the total debits and total credits
        return {
            'total_debits': total_debits,
            'total_credits': total_credits
        }
