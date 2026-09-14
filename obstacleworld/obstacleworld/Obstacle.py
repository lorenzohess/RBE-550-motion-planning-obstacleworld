#!/usr/bin/env python3


class Obstacle:
    def __init__(self, cells):
        self.cells = cells


def normalize(cells):
    """Shift cells so the minimum coordinates are zero. Returns a sorted tuple."""
    minX = min(cell[0] for cell in cells)
    minY = min(cell[1] for cell in cells)
    return tuple(sorted((cell[0] - minX, cell[1] - minY) for cell in cells))


def rotations(cells):
    """Return the distinct rotations of a shape, as normalized tuples."""
    distinct = []
    current = list(cells)
    for _ in range(4):
        # Rotate 90 degrees: (x, y) -> (y, -x)
        current = [(y, -x) for x, y in current]
        shape = normalize(current)
        if shape not in distinct:
            distinct.append(shape)
    return distinct


def allOrientations(obstacles):
    """Expand a list of obstacles into every distinct rotation of each."""
    shapes = []
    for obstacle in obstacles:
        for shape in rotations(obstacle.cells):
            if shape not in shapes:
                shapes.append(shape)
    return [Obstacle(list(shape)) for shape in shapes]


Ltet = Obstacle([(0, 0), (1, 0), (1, -1), (1, -2)])

Itet = Obstacle([(0, 0), (0, 1), (0, 2), (0, 3)])

Stet = Obstacle([(0, 0), (0, -1), (1, -1), (1, -2)])

Ttet = Obstacle([(0, 0), (1, 0), (1, 1), (1, -1)])
