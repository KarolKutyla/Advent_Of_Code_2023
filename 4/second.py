import re
import math

FILEPATH='input.txt'
#FILEPATH='test_input.txt'
extract_data = re.compile(r'Card\s+\d+:\s+((?:\d+\s+)*)\|\s*((?:\d+\s+)*)')


def count_result(current_numbers, winning_numbers):
    result=0
    for i in current_numbers:
        if i in winning_numbers:
            result+=1
    return result


with open(FILEPATH, 'r') as f:
    data = f.read()

sum = 0
card_descriptor=dict()
counter=1
for i in extract_data.findall(data):
    winning_numbers=set([int(j.group()) for j in re.finditer(r'\d+',i[0])])
    current_numbers=set([int(j.group()) for j in re.finditer(r'\d+',i[1])])
    card_descriptor[counter]=count_result(current_numbers, winning_numbers)
    counter+=1

solveing_list=[1 for i in range(1, counter)]
counter=1
while len(solveing_list) > 0:
    element = solveing_list.pop(0)
    for i in range(card_descriptor[counter]):
        solveing_list[i]+=element
    counter+=1
    sum+=element

print(sum)