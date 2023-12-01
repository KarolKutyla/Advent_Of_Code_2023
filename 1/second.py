import re

#filename="test_input_2.txt"
filename="input.txt"

_regex=re.compile('zero|one|two|three|four|five|six|seven|eight|nine|[0-9]')
_dict={'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
for i in range(10):
    _dict[str(i)]=i

def get_number(line):
    try:
        results=[i for i in _regex.finditer(line)]
        first = _dict[results[0].group()]*10
        last = _dict[results[-1].group()]
        x = _regex.findall(line[results[-1].start()+1:])
        if len(x) > 0:
            last = _dict[x[-1]]
        return first+last
    except Exception:
        print("There is no digit in line!")
        return 0


with open(filename, "r") as f:
    data=f.read().split('\n')

_sum = 0
for i in data:
    _sum += get_number(i)
print("Sum is", _sum)
