from flask import Blueprint, request, jsonify
from app.services.company_service import CompanyService

company_bp = Blueprint('company_bp', __name__)


@company_bp.route('/companies', methods=['POST'])
def add_company():
    data = request.get_json()
    try:
        CompanyService.add_company(data)
        return jsonify({'message': 'Company added successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@company_bp.route('/companies', methods=['GET'])
def get_companies():
    try:
        companies = CompanyService.get_companies()
        return jsonify(companies), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
