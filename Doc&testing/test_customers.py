import unittest
from app import create_app

class CustomerTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

    def test_create_customer(self):
        payload = {
            "name": "John Doe",
            "email": "john@email.com",
            "phone": "555-1234"
        }

        response = self.client.post(
            "/customers/",
            json=payload
        )

        self.assertEqual(response.status_code, 201)

    def test_get_customers(self):
        response = self.client.get("/customers/")

        self.assertEqual(response.status_code, 200)

    def test_get_customer_by_id(self):
        response = self.client.get("/customers/1")

        self.assertEqual(response.status_code, 200)

    def test_update_customer(self):
        payload = {
            "name": "Updated Name"
        }

        response = self.client.put(
            "/customers/1",
            json=payload
        )

        self.assertEqual(response.status_code, 200)

    def test_delete_customer(self):
        response = self.client.delete("/customers/1")

        self.assertEqual(response.status_code, 200)