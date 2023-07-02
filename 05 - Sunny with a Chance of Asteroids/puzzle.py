# https://adventofcode.com/2019/day/5

with open("input.in", "r") as file: 
    data = [int(x) for x in file.read().strip().split(',')]

def exe(program, inp):
    pointer = 0
    output = 0
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
            program[program[pointer + 1]] = inp
            pointer += 2
            continue

        if op_code == 4: # Output
            output = program[pointer + 1] if parameters['C'] == 1 else program[program[pointer + 1]]
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

def run_intcode(program, inp):
    if not program:
        program = list(data) # Clone data
        
    output = exe(program, inp)
    return output

if __name__ == '__main__':
    # part one
    print(run_intcode(None, 1))

    # part two
    print(run_intcode(None, 5))