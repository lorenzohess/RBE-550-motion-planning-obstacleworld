#!/usr/bin/env python3

import random

from .WorldGrid import WorldGrid, DEFAULT_WIDTH, DEFAULT_HEIGHT
from .Obstacle import Ltet, Itet, Stet, Ttet, allOrientations

TETS = allOrientations([Ltet, Itet, Stet, Ttet])


class World:
    def __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, rng=None):
        """Obstacle world. Pass rng (a random.Random) for reproducible generation."""
        self.grid = WorldGrid(width, height)
        self.rng = rng if rng is not None else random

    def placeRandomTetromino(self):
        """Fill cells with a tetromino shape. Wraps around the grid."""
        x = self.rng.randint(0, self.grid.width - 1)
        y = self.rng.randint(0, self.grid.height - 1)

        tet = self.rng.choice(TETS)

        for cell in tet.cells:
            cellX, cellY = cell[0], cell[1]
            gridX = (x + cellX) % self.grid.width
            gridY = (y + cellY) % self.grid.height
            self.grid.setOccupied(gridX, gridY)

    def coverage(self):
        return self.grid.nOccupiedCells() / self.grid.nCells

    def generateObstacleField(self, rho):
        """Generate a tetromino obstacle field with coverage rho."""
        if rho < 0 or rho > 1:
            raise ValueError("Rho must be between 0 and 1.")

        if rho == 0:
            self.grid.clearAll()
        elif rho == 1:
            self.grid.fillAll()
        else:
            # nObstacles = 0
            while self.coverage() < rho:
                self.placeRandomTetromino()
                # nObstacles += 1
            # print(nObstacles)
