import unittest
from unittest.mock import patch, MagicMock

import requests
from requests.exceptions import Timeout

from main_joke_1 import len_joke, get_joke


class TestJoke_1(unittest.TestCase):
    @patch('main_joke_1.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = "one"
        self.assertEqual(len_joke(), 3)

    @patch('main_joke_1.requests')
    def test_get_joke(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"value": "hello world"}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), "hello world")

    @patch('main_joke_1.requests')
    def test_fail_get_joke(self, mock_requests):
        mock_response = MagicMock(status_code=403)
        # mock_response.json.return_value = {"value": "hello world"}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), "No jokes")

    @patch('main_joke_1.requests')
    def test_get_joke_timeout_exception(self, mock_requests):
        mock_requests.exceptions = requests.exceptions
        mock_requests.get.side_effect = Timeout("Seems that the server is down")
        self.assertEqual(get_joke(), "No jokes")


if __name__ == '__main__':
    unittest.main()
