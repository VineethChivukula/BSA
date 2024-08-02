from app.utils.db import db

class Company(db.Model):
    __tablename__ = 'company'
    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'company_id': self.company_id,
            'company_name': self.company_name
        }
