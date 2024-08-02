from flask import Blueprint, request, jsonify
from app.services.bank_statement_service import BankStatementService

statement_bp = Blueprint('statement_bp', __name__)


@statement_bp.route('/generate_statement', methods=['POST'])
def generate_statement():
    data = request.get_json()
    try:
        BankStatementService.generate_statement(data)
        return jsonify({'message': 'Statement generated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@statement_bp.route('/upload_statement', methods=['POST'])
def upload_statement():
    data = request.get_json()
    try:
        BankStatementService.upload_statement(data)
        return jsonify({'message': 'Statement uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@statement_bp.route('/download_statements', methods=['POST'])
def download_statements():
    data = request.get_json()
    try:
        statements = BankStatementService.download_statements(data)
        return jsonify(statements), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
