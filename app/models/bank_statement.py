from app.utils.db import db

class BankStatement(db.Model):
    __tablename__ = 'bank_statement'
    statement_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.company_id'), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey('branch.branch_id'), nullable=False)
    statement_date = db.Column(db.Date, nullable=False)
    statement_data = db.Column(db.String(255), nullable=False)
    transactions = db.relationship('Transaction', backref='statement', lazy=True)
