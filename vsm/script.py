# pip3 install pdfplumber
import pdfplumber
import pandas as pd
import csv
from collections import defaultdict

columns = defaultdict(list)

# a single page
# with pdfplumber.open(r'test_data.pdf') as pdf:
#     first_page = pdf.pages[-0]
#     print(first_page.extract_text(), "<-----------data")

data = pd.read_csv('test_data_1.csv')
print(data, "<----data----")
# col = data.columns.join
# print(col)
# a = data[8:13]
# print(a, "<-------")
# for x in a:
#     print(x, "---")
# my_csv = pd.read_csv('test_data.csv')
# # print(my_csv.iloc[:, 1:-1].values)
# a = my_csv.iloc[:, -1].values
# with open('example.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(a)
