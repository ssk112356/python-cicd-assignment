from fastapi.testclient import TestClient
from app import app
import unittest

client = TestClient(app)

class TestAPI(unittest.TestCase):
    def test_read_root(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to the CI/CD Pipeline API!"})

    def test_add(self):
        response = client.get("/add/5/5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 10})

    if __name__ == '__main__':
        unittest.main()