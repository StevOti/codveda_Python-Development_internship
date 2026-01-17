import unittest
from unittest.mock import patch, Mock

from Level_2_Intermediate import data_scraper


class TestDataScraper(unittest.TestCase):
    @patch('Level_2_Intermediate.data_scraper.requests.get')
    def test_fetch_title_success(self, mock_get):
        mock_resp = Mock()
        mock_resp.status_code = 200
        mock_resp.text = '<html><head><title> My Page </title></head><body></body></html>'
        mock_resp.raise_for_status = Mock()
        mock_get.return_value = mock_resp

        title = data_scraper.fetch_title('http://example.com')
        self.assertEqual(title, 'My Page')

    @patch('Level_2_Intermediate.data_scraper.requests.get')
    def test_fetch_title_no_title(self, mock_get):
        mock_resp = Mock()
        mock_resp.status_code = 200
        mock_resp.text = '<html><body>No title here</body></html>'
        mock_resp.raise_for_status = Mock()
        mock_get.return_value = mock_resp

        title = data_scraper.fetch_title('http://example.com')
        self.assertIsNone(title)

    @patch('Level_2_Intermediate.data_scraper.requests.get')
    def test_fetch_text_error(self, mock_get):
        mock_get.side_effect = Exception('network')
        text = data_scraper.fetch_text('http://bad')
        self.assertIsNone(text)


if __name__ == '__main__':
    unittest.main()
