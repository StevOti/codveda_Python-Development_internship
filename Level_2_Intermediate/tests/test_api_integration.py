import unittest
from unittest.mock import patch, Mock

from Level_2_Intermediate import api_integration


class TestAPIIntegration(unittest.TestCase):
    @patch('Level_2_Intermediate.api_integration.requests.get')
    def test_fetch_json_success(self, mock_get):
        mock_resp = Mock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {'key': 'value'}
        mock_resp.raise_for_status = Mock()
        mock_get.return_value = mock_resp

        data = api_integration.fetch_json('http://api.example.com')
        self.assertIsInstance(data, dict)
        self.assertEqual(data['key'], 'value')

    @patch('Level_2_Intermediate.api_integration.requests.get')
    def test_fetch_json_error(self, mock_get):
        mock_get.side_effect = Exception('network')
        data = api_integration.fetch_json('http://bad')
        self.assertIsNone(data)


if __name__ == '__main__':
    unittest.main()
