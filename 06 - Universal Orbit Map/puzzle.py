# https://adventofcode.com/2019/day/6

with open("input.in", "r") as file: 
    data = file.read().split()

# Define a set of all objects in space
objects = { obj for item in data for obj in item.split(')') }
# Define a dictionary of each object where the value is the object of direct orbit 
links = { item.split(')')[1] : item.split(')')[0] for item in data }

def part_one():
    total_orbits = 0
    for obj in objects:
        total_orbits += count_orbits(obj, links, 0)
    return total_orbits

def part_two():
    you = get_orbits("YOU", links, None)
    san = get_orbits("SAN", links, None)

    return len(set(you.symmetric_difference(san)))

def get_orbits(obj, links, out):
    if not out: 
        out = set()
    if obj == "COM":
        return out 
    n = links[obj]
    out.add(n)
    return get_orbits(n, links, out)

def count_orbits(obj, links, count):
    if obj == "COM":
        return count 
    next = links[obj]
    count += 1
    return count_orbits(next, links, count)

if __name__ == '__main__':
    # part one
    print(part_one())

    # part two
    print(part_two())