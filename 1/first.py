#filename="test_input_1.txt"
filename="input.txt"


def get_number(line):
    try:
        for i in line:
            if i.isnumeric():
                first=i
                break

        for i in line[::-1]:
            if i.isnumeric():
                last=i
                break

        return int(first) * 10 + int(last)
    except Exception:
        print("There is no digit in line!")
        return 0


with open(filename, "r") as f:
    data=f.read().split('\n')

_sum = 0
for i in data:
    _sum += get_number(i)
print(_sum)
