import unittest
from unittest.mock import patch, MagicMock

import requests
from requests.exceptions import Timeout, HTTPError

from main_joke_2 import len_joke, get_joke


class TestJoke_2(unittest.TestCase):
    @patch('main_joke_2.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = "one"
        self.assertEqual(len_joke(), 3)

    @patch('main_joke_2.requests')
    def test_get_joke(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"value": "hello world"}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), "hello world")

    @patch('main_joke_2.requests')
    def test_fail_get_joke(self, mock_requests):
        mock_response = MagicMock(status_code=403)
        # mock_response.json.return_value = {"value": "hello world"}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), "No jokes")

    @patch('main_joke_2.requests')
    def test_get_joke_timeout_exception(self, mock_requests):
        mock_requests.exceptions = requests.exceptions
        mock_requests.get.side_effect = Timeout("Seems that the server is down")
        self.assertEqual(get_joke(), "No jokes")

    @patch('main_joke_2.requests')
    def test_get_joke_raise_for_status(self, mock_requests):

        mock_requests.exceptions = requests.exceptions
        mock_response = MagicMock(status_code=403)
        mock_response.raise_for_status.side_effect = HTTPError("Something gone wrong")
        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), "HTTPError was raised") # self.assertRaises(HTTPError, get_joke)


if __name__ == '__main__':
    unittest.main()
