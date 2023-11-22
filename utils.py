def find_matching_form(form_data, templates):
    for template in templates:
        template_fields = template.get("fields", {})
        match = all(
            field in form_data and form_data[field] == field_type
            for field, field_type in template_fields.items()
        )
        if match:
            return template.get("name")
    return None
