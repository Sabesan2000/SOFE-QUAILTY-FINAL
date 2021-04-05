import webbrowser
import unittest
import unittest.mock
from unittest.mock import patch
import webbrowser

class TestReview(unittest.TestCase):
    @patch('webbrowser.open')
    def test_normal_input(self, mock):

        result = {
          "title": "Way of kings",
          "Author": "Brandon Sanderson",
        }

        webbrowser.open('https://www.goodreads.com/search?utf8=%E2%9C%93&q=' + result["title"] +'&search_type=books')

        self.assertTrue(mock.called)

    @patch('webbrowser.open')
    def test_messy_input(self, mock):

        result = {
          "title": "asdawdawd",
          "Author": "asfdafw",
        }

        webbrowser.open('https://www.goodreads.com/search?utf8=%E2%9C%93&q=' + result["title"] +'&search_type=books')

        self.assertTrue(mock.called)

if __name__ == "__main__":
    unittest.main()
