# https://adventofcode.com/2019/day/3

import re

with open("input.in", "r") as file: 
    data = file.readlines()

directions = {
    'U' : (0,1),
    'R' : (1,0),
    'D' : (0,-1),
    'L' : (-1,0)
}

def part_one():
    SEEN = set()
    DISTANCES = []
    
    # Loop each cable
    for i in range(0, len(data)):
        instructions = data[i].strip().split(',')

        # Reset position at start of each wire
        position = (0, 0)

        for ins in instructions:
            matches = re.match('(\w)(\d+)', ins)
            direction = directions[matches.group(1)]
            steps = int(matches.group(2))

            # Calculate each next step
            for step in range(0, steps):
                new_position = tuple(position[i] + direction[i] for i in range(len(position)))
                position = new_position

                if i > 0 and position in SEEN: # Check wires crossing
                    DISTANCES.append(abs(position[0]) + abs(position[1]))
                if i == 0: # Add to seen only on the first cable
                    SEEN.add(position)
    return min(DISTANCES)

def part_two():
    SEEN = {}
    DISTANCES = []
    
    # Loop each cable
    for i in range(0, len(data)):
        instructions = data[i].strip().split(',')

        # Reset position at start of each wire
        position = (0, 0)
        total_steps = 0

        for ins in instructions:
            matches = re.match('(\w)(\d+)', ins)
            direction = directions[matches.group(1)]
            steps = int(matches.group(2))

            # Calculate each next step
            for step in range(0, steps):
                new_position = tuple(position[i] + direction[i] for i in range(len(position)))
                position = new_position
                total_steps += 1

                if i > 0 and position in SEEN: # Check wires crossing
                    DISTANCES.append(total_steps + SEEN[position])
                if i == 0: # Add to seen only on the first cable
                    SEEN[position] = total_steps
    return min(DISTANCES)

if __name__ == '__main__':
    # part one
    part_one()

    # part two
    part_two()
