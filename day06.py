import copy
data = [line for line in open('input.txt').read().splitlines()]

# part 1.
orbit_collection = []
orbit_elements = []
for element in data:
    orbit_ends = element.split(')')
    orbit_elements.extend([orbit_ends[0], orbit_ends[1]])
    orbit_collection.append((orbit_ends[0], orbit_ends[1]))
orbit_collection = set(orbit_collection)
_input = orbit_collection.copy()
orbit_elements = set(orbit_elements)
count = 0
while True:
    count += 1
    if count == 10:
        break
    new_set = [x for x in orbit_collection.copy()]
    for orbit in orbit_collection:
        for element in orbit_elements:
            indirect_pair =  (element, orbit[0])
            if indirect_pair in orbit_collection:
                new_set.append((element, orbit[1]))
    new_set = set(new_set)
    if len(orbit_collection) == len(new_set):
        break
    else:
        orbit_collection = new_set

# part 2
data = [(val.split(')')[0], val.split(')')[1]) for val in data]

# starting postion
positions = [(x, y) for (x,y) in data if 'YOU' in (x, y)]

steps = 0

# collect postions already passed to avoid looping paths.
used_positions = []

# loop by finding next possible positions from each orbit in the way.
# until SAN is reached and exit printing number of orbits between.
while True:
    steps += 1
    new_positions = []
    for position in positions:
        if position in used_positions:
            continue
        used_positions.append(position)
        if 'SAN' in position:
            print steps-2
            exit()
        new_positions += [(x,y) for (x, y) in data
                         if x in position or y in position]
    # move to latest positions.
    positions = copy(new_positions)
