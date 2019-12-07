import re
class Travel(object):
    def __init__(self, journey):
        self.coordinates = []
        self.current_location = (0,0)
        self.journey = journey.split(',')
        for path in self.journey:
            self.build_coordinates(path)

    def build_coordinates(self, path):
        _match_obj = re.match('(\w)(\d+)', path)
        _direction = _match_obj.group(1)
        _distance = _match_obj.group(2)
        if _direction is 'R':
            self.take_right(_distance)
        if _direction is 'L':
            self.take_left(_distance)
        if _direction is 'U':
            self.take_up(_distance)
        if _direction is 'D':
            self.take_down(_distance)
        return


    def take_right(self, distance):
        _x, _y = self.current_location
        for i in range(int(distance)):
            _y += 1
            self.coordinates.append((_x, _y))
        self.current_location = _x, _y

    def take_left(self, distance):
        _x, _y = self.current_location
        for i in range(int(distance)):
            _y -= 1
            self.coordinates.append((_x, _y))
        self.current_location = _x, _y

    def take_up(self, distance):
        _x, _y = self.current_location
        for i in range(int(distance)):
            _x += 1
            self.coordinates.append((_x, _y))
        self.current_location = _x, _y

    def take_down(self, distance):
        _x, _y = self.current_location
        for i in range(int(distance)):
            _x -= 1
            self.coordinates.append((_x, _y))
        self.current_location = _x, _y

_input = open('input.txt').read().splitlines()

journey1 = _input[0]
journey2 = _input[1]

travel_1 = Travel(journey1)
travel_2 = Travel(journey2)
print 'created co-ordiantes'

def manhattan_dist(_x, _y):
    return abs(_x) + abs(_y)

# find intersections.
_intersection_coords = set(travel_1.coordinates).intersection(set(travel_2.coordinates))

# part 1
_min_manhattan_dist_to_intersection = min([manhattan_dist(x, y) for x,y in _intersection_coords])

# part 2
step_counts = []
for x,y in _intersection_coords:
    travel1_steps = travel_1.coordinates.index((x,y)) + 1
    travel2_steps = travel_2.coordinates.index((x,y)) + 1
    step_counts.append(travel1_steps+travel2_steps)

print min(step_counts)
