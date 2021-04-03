from parameterized import parameterized
from datetime import datetime
from PyPDF2.pdf import PdfFileReader
import unittest
import csv
import sys

test_data = []

def get_pdf_page(file_path):
    pdf = PdfFileReader(file_path)
    return pdf.getNumPages()

# read from file containing values to test and store in array test_data
def init_test_data(filename):
    with open(filename, newline='\n') as data:
        reader = csv.reader(data, delimiter=',')
        line_no = 0;
        for row in reader:
            if line_no > 0:
                try:
                    d = [row[0].split('.')[0], row[0], int(row[1])]
                    test_data.append(d)
                except:
                    pass
            line_no += 1

# must be done before test sequence is defined!
init_test_data("test-data.csv")

class TestSequence(unittest.TestCase):
    @parameterized.expand(test_data)
    def test_page_count(self, name, filename, pages):
        actual_pages = get_pdf_page(f"TestPDFs/{filename}")
        unittest.TestCase.assertEqual(self, first=pages, second=actual_pages, msg=name)



if __name__ == '__main__':
    # get the data for the tests from the specified csv

    with open(f'DynamicTestData/t-{datetime.now().strftime("%Y-%m-%dT%H%M%S")}.txt', "w") as output:
        runner = unittest.TextTestRunner(output)
        unittest.main(testRunner=runner)


