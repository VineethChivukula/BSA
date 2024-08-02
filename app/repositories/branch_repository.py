from app.models.branch import Branch
from app.utils.db import db

class BranchRepository:
    @staticmethod
    def add_branch(data):
        new_branch = Branch(**data)
        db.session.add(new_branch)
        db.session.commit()

    @staticmethod
    def get_branches():
        branches = Branch.query.all()
        return [branch.to_dict() for branch in branches]

    @staticmethod
    def get_branch_by_name_and_company(branch_name, company_id):
        return Branch.query.filter_by(branch_name=branch_name, company_id=company_id).first()

    @staticmethod
    def get_default_branch_for_company(company_id):
        return Branch.query.filter_by(company_id=company_id).first()
