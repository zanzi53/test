import unittest
from app import app


class AppTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Flask on Wasmer", response.data)

    def test_greeting(self):
        response = self.client.get("/api/hello", query_string={"name": "太郎"})
        self.assertEqual(response.get_json()["message"], "こんにちは、太郎！")

    def test_empty_name(self):
        self.assertEqual(self.client.get("/api/hello?name=").get_json()["message"], "こんにちは、世界！")

    def test_long_name(self):
        self.assertEqual(self.client.get("/api/hello", query_string={"name": "x" * 101}).status_code, 400)

    def test_health(self):
        self.assertEqual(self.client.get("/healthz").get_json(), {"status": "ok"})


if __name__ == "__main__":
    unittest.main()
