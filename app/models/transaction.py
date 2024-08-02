from app.utils.db import db

class Transaction(db.Model):
    __tablename__ = 'transaction'
    transaction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    statement_id = db.Column(db.Integer, db.ForeignKey('bank_statement.statement_id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey('branch.branch_id'), nullable=False)
    branch = db.relationship('Branch', backref=db.backref('transactions', lazy=True))
