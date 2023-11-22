import re


def validate_template_data(template_data):
    allow_field_types = ['email', 'phone', 'date', 'text']

    if "name" not in template_data:  # Обязательный параметр
        return False, "Missing 'name' field"

    template_data = [[field, field_type] for field, field_type in template_data.items() if field != "name"]
    for field, field_type in template_data:
        if field_type not in ['email', 'phone', 'date', 'text']:
            return False, f"Invalid format in field '{field_type}', correct types: {allow_field_types}"

    return True, None


def get_type_by_values(form_data):
    field_types = {}
    for field, value in form_data.items():
        if validate_date(value):
            field_types[field] = "date"
        elif validate_phone(value):
            field_types[field] = "phone"
        elif validate_email(value):
            field_types[field] = "email"
        else:
            field_types[field] = "text"

    return field_types


def validate_field_type(field, field_type):
    if field_type == "email":
        return validate_email(field)
    elif field_type == "phone":
        return validate_phone(field)
    elif field_type == "date":
        return validate_date(field)
    elif field_type == "text":
        return True
    else:
        return False


def validate_email(email):
    # email
    return re.match(r'^[\w\.-]+@[\w\.-]+$', email) is not None


def validate_phone(phone):
    # +7 xxx xxx xx xx
    return re.match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', phone) is not None


def validate_date(date):
    # DD.MM.YYYY or YYYY-MM-DD
    return re.match(r'^\d{2}.\d{2}.\d{4}$|^\d{4}-\d{2}-\d{2}$', date) is not None
