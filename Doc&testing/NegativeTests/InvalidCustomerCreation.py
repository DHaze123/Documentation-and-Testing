def test_create_customer_invalid(self):
    payload = {
        "email": "bad@email.com"
    }

    response = self.client.post(
        "/customers/",
        json=payload
    )

    self.assertEqual(response.status_code, 400)