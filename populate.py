import requests

count_url = "http://flask-app:5000/get_forms_count"
add_url = "http://flask-app:5000/add_template"

forms = [
    {
        "name": "OrderForm",
        "order_email": "email",
        "order_phone": "phone",
        "birthday": "date"
    },
    {
        "name": "BackCallForm",
        "contact_email": "email",
        "contact_phone": "phone",
        "message": "text",
        "created_date": "date"
    },
    {
        "name": "ReviewForm",
        "author": "email",
        "review": "text"
    }
]

response = requests.get(count_url)
forms_count = response.json().get("count", 0)

if forms_count == 0:
    for form in forms:
        response = requests.post(add_url, json=form)
        print(f"Form {form['name']} added. Response: {response.status_code}")
else:
    print(f"There are already {forms_count} forms in the database. No new forms added.")
