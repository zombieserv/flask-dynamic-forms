import unittest
import requests


class TestGetFormAPI(unittest.TestCase):
    def setUp(self):
        self.url = "http://flask-app:5000"

    def test_valid_data_order_form(self):
        form_data = {"order_email": "user@gmail.com", "order_phone": "+7 123 456 78 90", "birthday": "27.06.1997"}
        response = requests.post(f'{self.url}/get_form', json=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('template'), 'OrderForm')

    def test_valid_data_order_form_with_any_field(self):
        form_data = {"order_email": "user@gmail.com", "order_phone": "+7 123 456 78 90", "birthday": "27.06.1997",
                     "avatar": "https://imgur.com"}
        response = requests.post(f'{self.url}/get_form', json=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('template'), 'OrderForm')

    def test_valid_incomplete_data_order_form(self):
        form_data = {"order_email": "user@gmail.com", "order_phone": "+7 123 456 78 90"}
        response = requests.post(f'{self.url}/get_form', json=form_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"order_email": "email", "order_phone": "phone"})

    def test_invalid_data_order_form(self):
        form_data = {"order_email": "Hello where!", "order_phone": "+7 123 456 78 90", "birthday": "27.06.1997"}
        response = requests.post(f'{self.url}/get_form', json=form_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"birthday": "date", "order_email": "text", "order_phone": "phone"})

    def test_valid_data_back_call_form(self):
        form_data = {"contact_email": "user@gmail.com", "contact_phone": "+7 123 456 78 90", "message": "Hello!",
                     "created_date": "2023-11-21"}
        response = requests.post(f'{self.url}/get_form', json=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('template'), 'BackCallForm')

    def test_valid_data_back_call_form_with_any_field(self):
        form_data = {"contact_email": "user@gmail.com", "contact_phone": "+7 123 456 78 90", "message": "Hello!",
                     "created_date": "2023-11-21", "g-response": "1q2w3e4r5t6y"}
        response = requests.post(f'{self.url}/get_form', json=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('template'), 'BackCallForm')

    def test_valid_incomplete_data_back_call_form(self):
        form_data = {"contact_email": "user@gmail.com", "contact_phone": "+7 123 456 78 90"}
        response = requests.post(f'{self.url}/get_form', json=form_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"contact_email": "email", "contact_phone": "phone"})

    def test_invalid_data_back_call_form(self):
        form_data = {"contact_email": "user@gmail.com", "contact_phone": "Russia", "message": "Hello!",
                     "created_date": "Today"}
        response = requests.post(f'{self.url}/get_form', json=form_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"contact_email": "email", "contact_phone": "text",
                                           "created_date": "text", "message": "text"})

    def test_valid_data_review_form(self):
        form_data = {"author": "user@gmail.com", "review": "Great product!"}
        response = requests.post(f'{self.url}/get_form', json=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('template'), 'ReviewForm')

    def test_valid_data_review_form_with_any_field(self):
        form_data = {"author": "user@gmail.com", "review": "Great product!", "rating": "5"}
        response = requests.post(f'{self.url}/get_form', json=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('template'), 'ReviewForm')

    def test_valid_incomplete_data_review_form(self):
        form_data = {"author": "user@gmail.com"}
        response = requests.post(f'{self.url}/get_form', json=form_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"author": "email"})

    def test_invalid_data_review_form(self):
        form_data = {"author": "Not an email", "review": "Great product!"}
        response = requests.post(f'{self.url}/get_form', json=form_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"author": "text", "review": "text"})


if __name__ == '__main__':
    unittest.main()
