import webbrowser
import unittest
import unittest.mock
from unittest.mock import MagicMock
from unittest.mock import patch
import webbrowser

class TestReview(unittest.TestCase):
    @patch('webbrowser.open')
    def test_open_page(self, mock):
        results = []

        result1 = {
          "title": "Way of kings",
          "Author": "Brandon Sanderson",
        }

        result2 = {
          "title": "asdawdawd",
          "Author": "asfdafw",
        }

        result3 = {
          "title": "The Sport Of Kings",
          "Author": "C.E. Morgan",
        }

        results.append(result1)
        results.append(result2)
        results.append(result3)

        for result in results:
            webbrowser.open('https://www.goodreads.com/search?utf8=%E2%9C%93&q=' + result["title"] +'&search_type=books')

        self.assertEqual(mock.call_count, 3)

if __name__ == "__main__":
    unittest.main()
