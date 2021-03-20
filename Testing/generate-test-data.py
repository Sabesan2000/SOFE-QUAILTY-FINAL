# Create a CSV file containing the test pdf names and their respective page numbers

from os import listdir
from PyPDF2.pdf import PdfFileReader
import csv


test_dir = 'TestPDFs'

pdf_names = listdir(test_dir)
page_counts = []

for name in pdf_names:
    with open(f'{test_dir}/{name}', "rb") as pdf_file:
        pdf_reader = PdfFileReader(pdf_file)
        page_counts.append(pdf_reader.numPages)

with open('test-data.csv', 'w', newline='\n') as out_file:
    writer = csv.writer(out_file)
    col_names = ["filename", "pagecount"]
    writer.writerow(col_names)
    for data in zip(pdf_names, page_counts):
        writer.writerow(data)







