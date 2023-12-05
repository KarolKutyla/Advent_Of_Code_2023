import re
import math

FILEPATH='input.txt'
#FILEPATH='test_input.txt'
extract_data = re.compile(r'Card\s+\d+:\s+((?:\d+\s+)*)\|\s*((?:\d+\s+)*)')

with open(FILEPATH, 'r') as f:
    data = f.read()


def count_result(current_numbers, winning_numbers):
    result=0
    for i in current_numbers:
        if i in winning_numbers:
            result+=1
    return int(math.pow(2, result)/2)


sum = 0
for i in extract_data.findall(data):
    winning_numbers=set([int(j.group()) for j in re.finditer(r'\d+',i[0])])
    current_numbers=set([int(j.group()) for j in re.finditer(r'\d+',i[1])])
    sum+=count_result(current_numbers, winning_numbers)
print(sum)