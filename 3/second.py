import re

#input_path="test_input.txt"
input_path="input.txt"
number_regex=re.compile(r'(\d+)')
sign_regex=re.compile(r'\*')

def gen_number_of_indexs(star_x, number_iterator):
    vals = []
    for i in number_iterator:
        pos_left=i.span()[0] - 1
        pos_right=i.span()[1]
        if pos_left <= star_x <= pos_right:
            vals+=[i.group()]
    return vals

def through_one_line(line_iter, num_iters):
    sum = 0
    for i in line_iter:
        num_list = []
        for j in num_iters:
            num_list+=gen_number_of_indexs(i.span()[0], j)
        if len(num_list) == 2:
            sum+=int(num_list[0])*int(num_list[1])
    return sum

def count_sum(data):
    sum=0
    sign_iters=[]
    num_iters=[]
    for i in data:
        sign_iters+=[[i for i in sign_regex.finditer(i)]]
        num_iters+=[[i for i in number_regex.finditer(i)]]
    sum += through_one_line(sign_iters[0], num_iters[0:2])
    for i in range(1, len(sign_iters)-1):
        sum+=through_one_line(sign_iters[i], num_iters[i-1:i+2])
    sum += through_one_line(sign_iters[-1], num_iters[-2:])
    return sum



with open(input_path, "r") as f:
    data=f.read().split('\n')
print(count_sum(data))



