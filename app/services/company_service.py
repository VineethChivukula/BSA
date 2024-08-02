from app.repositories.company_repository import CompanyRepository

class CompanyService:
    @staticmethod
    def add_company(data):
        try:
            CompanyRepository.add_company(data)
        except Exception as e:
            raise Exception(f"Error adding company: {str(e)}")

    @staticmethod
    def get_companies():
        try:
            companies = CompanyRepository.get_companies()
            return companies
        except Exception as e:
            raise Exception(f"Error retrieving companies: {str(e)}")
