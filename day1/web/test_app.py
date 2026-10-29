import unittest
from unittest.mock import patch
from app import app


class TestHealthEndpoint(unittest.TestCase):

    @patch("app.get_connection")
    def test_health_when_database_is_available(self, mock_connection):
        response = app.test_client().get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["database"], "ok")

    @patch("app.get_connection", side_effect=Exception("DB unavailable"))
    def test_health_when_database_is_unavailable(self, mock_connection):
        response = app.test_client().get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertIn("error:", response.get_json()["database"])


if __name__ == "__main__":
    unittest.main()
