import re
#filepath = 'test_input.txt'
filepath = 'input.txt'

start_regex=re.compile(r'Game\s([0-9]+)')
game_regex=re.compile(r'(\d+) ([a-z]+)')
id_sum=0
cubes={'blue': 14, 'red': 12, 'green': 13}


def is_game_possible(game):
    result=game_regex.findall(game)
    for r in result:
        if int(r[0]) > cubes[r[1]]:
            return False
    return True


def extract_data(line):
    global id_sum
    line=line.split(': ')
    begin=line[0]
    games=line[1].split(';')
    for i in games:
        if not is_game_possible(i):
            return
    id_sum += int(start_regex.findall(begin)[0])


with open(filepath, 'r') as f:
    data = f.read().split('\n')
for i in data:
    extract_data(i)
print(id_sum)
