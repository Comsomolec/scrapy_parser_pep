import re

text = 'PEP 1 – PEP Purpose and Guidelines'


title = re.search(r'(?P<number>\d+)\W+(?P<name>.+)', text)
print(title.group('name'))