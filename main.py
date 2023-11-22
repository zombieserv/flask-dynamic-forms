from env import *
from flask import Flask, request, jsonify
from middleware import validate_middleware
from models import DynamicForm
from utils import find_matching_form
from validate import get_type_by_values

app = Flask(__name__)

app.before_request(validate_middleware)


@app.route('/add_template', methods=['POST'])
def add_template():
    template_data = request.get_json()
    fields_dict = {field: template_data[field] for field in template_data if field != "name"}

    form = DynamicForm(name=template_data['name'], fields=fields_dict)
    form.save()

    return jsonify({"message": "Template added successfully"}), 201


@app.route('/get_form', methods=['POST'])
def get_form():
    form_data = request.get_json()

    types = get_type_by_values(form_data)
    print(types)

    forms = DynamicForm.get_all_forms()

    matching_template_name = find_matching_form(types, forms)
    if matching_template_name:
        return jsonify({"template": matching_template_name}), 200

    return jsonify(types), 404


@app.route('/get_forms_count', methods=['GET'])
def get_forms_count_endpoint():
    forms = DynamicForm.get_all_forms()
    return jsonify({"count": len(forms)})


if __name__ == '__main__':
    app.run(host=os.getenv("APP_URL"), port=os.getenv("APP_PORT"), debug=True)
