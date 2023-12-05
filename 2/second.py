import re
#filepath = 'test_input.txt'
filepath = 'input.txt'
start_regex = re.compile(r'Game\s([0-9]+)')
game_regex = re.compile(r'(\d+) ([a-z]+)')
_sum = 0


def find_minimal_amount(game, _cubes):
    result=game_regex.findall(game)
    for r in result:
        val = int(r[0])
        if val > _cubes[r[1]]:
            _cubes[r[1]]=val
    return True


def extract_data(line):
    global _sum
    _cubes = {'blue': 0, 'red': 0, 'green': 0}
    line = line.split(': ')
    games = line[1].split(';')
    for i in games:
        find_minimal_amount(i, _cubes)

    j = 1
    for i in _cubes.values():
        j *= i
    _sum += j


with open(filepath, 'r') as f:
    data = f.read().split('\n')
for i in data:
    extract_data(i)
print(_sum)