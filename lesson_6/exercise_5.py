from collections import namedtuple
import math

Point = namedtuple('Point', ['x', 'y'])

p1 = Point(x=1, y=2)
p2 = Point(4, 6)

# Print Point
print(p1)
print(p2)

# Generate a board
board = [["-"]*10 for i in range(10)]

# mark x, y in board as *
board[1][2] = '*'
board[4][6] = '*'

# Print board
for row in board:
    print(row)

# mark x, y in board as *
board[p1.x][p1.y] = '*'
board[p2.x][p2.y] = '*'

# Calculate the Euclidean distance for p1 and p2
delta_x = abs(p1.x - p2.x)
delta_y = abs(p1.y - p2.y)
c = math.sqrt((delta_x**2) + (delta_y**2))
print(c)