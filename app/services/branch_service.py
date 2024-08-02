from app.repositories.branch_repository import BranchRepository

class BranchService:
    @staticmethod
    def add_branch(data):
        try:
            BranchRepository.add_branch(data)
        except Exception as e:
            raise Exception(f"Error adding branch: {str(e)}")

    @staticmethod
    def get_branches():
        try:
            branches = BranchRepository.get_branches()
            return branches
        except Exception as e:
            raise Exception(f"Error retrieving branches: {str(e)}")
