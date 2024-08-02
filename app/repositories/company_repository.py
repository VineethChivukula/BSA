from app.models.company import Company
from app.utils.db import db

class CompanyRepository:
    @staticmethod
    def get_company_by_name(company_name):
        return Company.query.filter_by(company_name=company_name).first()
