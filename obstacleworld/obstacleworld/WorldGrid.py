#!/usr/bin/env python3

import numpy as np

DEFAULT_WIDTH = 128
DEFAULT_HEIGHT = 128

EMPTY = 0
OCCUPIED = 1


class WorldGrid:
    def __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
        """The world grid is a numpy array. Value 0 is empty, value 1 is occupied."""
        self.width = width
        self.height = height

        self.nCells = self.width * self.height

        self.cells = np.zeros((height, width), dtype=np.int8)

    def get(self, x, y):
        return self.cells[y, x]

    def set(self, x, y, value):
        self.cells[y, x] = value

    def setOccupied(self, x, y):
        self.set(x, y, OCCUPIED)

    def clearAll(self):
        self.cells.fill(EMPTY)

    def fillAll(self):
        self.cells.fill(OCCUPIED)

    def nOccupiedCells(self):
        """Return number of occupied cells."""
        return np.count_nonzero(self.cells)
