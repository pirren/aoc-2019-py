# https://adventofcode.com/2019/day/7

import itertools 
import sys
sys.set_int_max_str_digits(0)

with open("input.in", "r") as file: 
    data = [int(x) for x in file.read().strip().split(',')]

# Five amplifiers in series leading to thrusters
# First amplifier input is 0

def exe(program, inp, phase_setting):
    pointer = 0
    output = 0
    has_done_input = False # Flag for first input occurence
    while True:
        instruction = program[pointer]
        # Extract opcode
        op_code = int(str(instruction)[-2:])
        if op_code == 99: # Program finished
            return output # Return last output
        
        # Extract parameter mode
        parameters = { 
            'C' : (instruction // 100) % 10,
            'B' : (instruction // 1000) % 10, 
            'A' : (instruction // 10000) % 10 
        }

        if op_code == 3: # Input
            program[program[pointer + 1]] = inp if has_done_input else phase_setting
            has_done_input = True # Set the first input occurence to complete
            pointer += 2
            continue

        if op_code == 4: # Output
            output = program[pointer + 1] if parameters['C'] == 1 else program[program[pointer + 1]]
            #print(f"output {output}")
            pointer += 2
            continue

        a = program[pointer + 1] if parameters['C'] == 1 else program[program[pointer + 1]] # First param
        b = program[pointer + 2] if parameters['B'] == 1 else program[program[pointer + 2]] # Second param
        jmp = False # Jump flag - indicates whether program has jumped - will not increase pointer
        value = None # Define value

        if op_code == 1: # Addition
            value = a + b
        if op_code == 2: # Multiplication
            value = a * b
        if op_code == 5: # Jump if true
            if a != 0:
                pointer = b
                jmp = True
        if op_code == 6: # Jump if false
            if a == 0:
                pointer = b
                jmp = True
        if op_code == 7: # Less than
            value = 1 if a < b else 0
        if op_code == 8: # Equals
            value = 1 if a == b else 0
        
        if jmp:
            continue

        # Failed jump, move on
        if value == None:
            pointer += 3
            continue

        # Store the value
        program[program[pointer + 3]] = value

        pointer += 4

def run_intcode(phase_settings):
    # io_signal starts as zero and is overwritten by the final output and entered into the next amplifier
    results = set()

    permutations = list(itertools.permutations(phase_settings))
    for combination in permutations:
        io_signal = 0
        for phase_setting in combination:
            program = list(data) # Restart software between amplifiers
            io_signal = exe(program, io_signal, phase_setting)
        
        results.add(io_signal)

    return max(results) if results else "no results"


if __name__ == '__main__':
    # part one
    print(run_intcode([0,1,2,3,4]))

    # part two
    print(run_intcode([5,6,7,8,9]))