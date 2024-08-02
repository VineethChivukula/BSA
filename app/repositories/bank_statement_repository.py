from app.models.bank_statement import BankStatement
from app.utils.db import db

class BankStatementRepository:
    @staticmethod
    def save_statement(data, s3_url):
        new_statement = BankStatement(
            user_id=data['user_id'],
            company_id=data['company_id'],
            branch_id=data['branch_id'],
            statement_date=data['statement_date'],
            statement_data=s3_url
        )
        db.session.add(new_statement)
        db.session.commit()

    @staticmethod
    def get_statement_id(data):
        statement = BankStatement.query.filter_by(
            user_id=data['user_id'],
            company_id=data['company_id'],
            branch_id=data['branch_id'],
            statement_date=data['statement_date'],
            statement_data=data['statement_data']
        ).first()
        return statement.statement_id if statement else None
