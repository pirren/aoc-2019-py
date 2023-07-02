# https://adventofcode.com/2019/day/2

import queue

with open("input.in", "r") as file: 
    data = [int(x) for x in file.read().strip().split(',')]

def run_intcode(instructions):
    for pointer in range(0, len(data), 4):
        
        op_code = instructions[pointer]
        if op_code == 99: # Program finished
            return instructions[0]

        a, b, position = [instructions[x] for x in range(pointer + 1, pointer + 4)]

        if op_code == 1: # Addition
            instructions[position] = instructions[a] + instructions[b]
        if op_code == 2: # Multiplication
            instructions[position] = instructions[a] * instructions[b]

def part_one():
    instructions = data.copy()
    instructions[1] = 12
    instructions[2] = 2

    return run_intcode(instructions)

def part_two():
    target_output = 19690720
    R = range(100)

    for noun in R:
        for verb in R:
            instructions = data.copy()
            instructions[1] = noun
            instructions[2] = verb
            
            output = run_intcode(instructions)

            if output == target_output:
                return 100 * noun + verb

if __name__ == '__main__':
    # part one
    print(part_one())

    # part two
    print(part_two())