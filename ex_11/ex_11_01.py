import urllib.request
import re
# example = input('Enter a regular expression: ')
#
# with open('C:\\Users\\Deadp\\Desktop\\Python\\lessons\\text_files\\mbox.txt') as file:
#     file = file.readlines()
# count = 0
# for line in file:
#     if line.startswith(example):
#         count=+1
#
# print(f'mbox_txt had {count} lines that matched {example}')
#file = urllib.request.urlopen('http://py4e-data.dr-chuck.net/regex_sum_42.txt')
file = urllib.request.urlopen('http://py4e-data.dr-chuck.net/regex_sum_1439416.txt')
lines = ''
for line in file:
    lines += line.decode()

total_of_digits = re.findall('[0-9]+',lines)
sum_of_digits = sum([int(n) for n in total_of_digits])
print(f'There are {len(total_of_digits)} values with a sum = {sum_of_digits}')
