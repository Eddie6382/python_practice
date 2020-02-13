import re

msg = 'please call my secretrary using 02-26669999'
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.search(pattern, msg)
print(phoneNum.group())

msg = 'Johnson, Johnnason, Johnnathan, Johnsonsonson will attend my party tonight'
pattern = 'John(son{1,3}|nason|nathan)'
txts = re.findall(pattern, msg, re.I)
for i in txts:
    print('John'+i)
