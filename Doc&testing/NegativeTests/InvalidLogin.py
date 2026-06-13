def test_invalid_login(self):
    payload = {
        "email": "fake@email.com",
        "password": "wrong"
    }

    response = self.client.post(
        "/auth/login",
        json=payload
    )

    self.assertEqual(response.status_code, 401)