def test_missing_token(self):
    response = self.client.post(
        "/service-tickets/",
        json={}
    )

    self.assertEqual(response.status_code, 401)