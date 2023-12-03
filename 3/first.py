import re

#input_path="test_input.txt"
input_path="input.txt"
number_regex=re.compile(r'(\d+)')
sign_regex=re.compile(r'[^\d.]')

def is_number_connected(number_pos, iterator):
    for i in iterator:
        pos=i.span()[0]
        if number_pos[0] - 1 <= pos <= number_pos[1]:
            return True
    return False

def through_one_line(num_iter, line_iters):
    sum = 0
    for i in num_iter:
        for j in line_iters:
            if is_number_connected(i.span(), j):
                sum+=int(i.group())
                break
    return sum

def count_sum(data):
    sum=0
    sign_iters=[]
    num_iters=[]
    for i in data:
        sign_iters+=[[i for i in sign_regex.finditer(i)]]
        num_iters+=[[i for i in number_regex.finditer(i)]]
    sum += through_one_line(num_iters[0], sign_iters[0:2])
    for i in range(1, len(num_iters)-1):
        sum+=through_one_line(num_iters[i], sign_iters[i-1:i+2])
    sum += through_one_line(num_iters[-1], sign_iters[-2:])
    return sum



with open(input_path, "r") as f:
    data=f.read().split('\n')
print(count_sum(data))



