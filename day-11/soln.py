import math

def sin(angle):
    return round(math.sin(math.radians(angle)))
def cos(angle):
    return round(math.cos(math.radians(angle)))

def turtle(input):
    wx, wy = 10, 1 # waypoint
    sx, sy = 0, 0 # ship
    lines  = [(line[0], int(line[1:]))for line in input.strip().split()]
    angle = 90
    for direction, amount in lines:
        if direction == 'N':
            wy += amount
        if direction == 'S':
            wy -= amount
        if direction == 'E':
            wx += amount
        if direction == 'W':
            wx -= amount
        if direction == 'F':
            sx += wx * amount
            sy += wy * amount
        if direction == 'L':
            wx, wy = wx * cos(amount) - wy * sin(amount), sin(amount) * wx + wy * cos(amount)
        if direction == 'R':
            wx, wy = wx * cos(-amount) - wy * sin(-amount), sin(-amount) * wx + wy * cos(-amount)
    print(abs(sx) + abs(sy))

turtle(open('test.txt').read())
turtle(open('real.txt').read())
