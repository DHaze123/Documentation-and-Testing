def test_customer_not_found(self):
    response = self.client.get("/customers/9999")

    self.assertEqual(response.status_code, 404)