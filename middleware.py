from flask import request, jsonify
from validate import validate_template_data


def validate_middleware():
    if request.endpoint == 'add_template':
        template_data = request.get_json()
        is_valid, error_message = validate_template_data(template_data)
        if not is_valid:
            return jsonify({"error": error_message}), 400
