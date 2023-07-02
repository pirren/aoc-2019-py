# https://adventofcode.com/2019/day/4

import re

with open("input.in", "r") as file: 
    data = file.read()

def check_phrase(phrase, part):
    # Check phrase length
    if len(phrase) != 6:
        return False

    # Check no decrement
    last = int(phrase[0])
    for x in range(1, len(phrase)):
        c = int(phrase[x])
        if last > c:
            return False
        last = c

    # Check two consecutive
    if part == 1:
        pattern = r'(\d)\1'
        if not re.search(pattern, phrase):
            return False
    else:
        in_sequence = []
        last = phrase[0]
        count = 1
        for x in range(1, len(phrase)):
            current = phrase[x]
            if last == current:
                count += 1
            else: 
                in_sequence.append(count)
                count = 1
                last = current
        in_sequence.append(count)
        if not 2 in in_sequence:
            return False

    return True

def check_passwords(part):
    min, max = map(int, data.split('-'))

    ok_passwords = 0

    for x in range(min, max + 1):
        phrase = str(x)
        if check_phrase(phrase, part):
            ok_passwords += 1
    return ok_passwords

if __name__ == '__main__':
    # part one
    print(check_passwords(1))

    # part two
    print(check_passwords(2))