# obstacleworld

Random tetromino obstacle fields on a rectangular grid. Written for RBE-550
assignment 1 (obstacle field figures) and reused by assignment 2 (*Flatland*),
which symlinks this directory rather than vendoring a copy.

## Usage

```python
import random
from obstacleworld.obstacleworld.World import World

world = World(64, 64, rng=random.Random(7))
world.generateObstacleField(0.2)

world.grid.cells        # numpy int8 array, shape (height, width), 0 empty / 1 occupied
world.coverage()        # fraction of occupied cells
```

The doubled `obstacleworld.obstacleworld` is not a typo: the outer directory is an
implicit namespace package (no `__init__.py`), so the import path repeats the name.

## API

**`WorldGrid(width=128, height=128)`**
`get(x, y)`, `set(x, y, value)`, `setOccupied(x, y)`, `clearAll()`, `fillAll()`,
`nOccupiedCells()`, and the attributes `width`, `height`, `nCells`, `cells`.

**`World(width=128, height=128, rng=None)`**
`generateObstacleField(rho)` places random tetrominoes until coverage reaches
`rho`; `coverage()`; `placeRandomTetromino()`. Passing `rho` outside `[0, 1]`
raises `ValueError`; `0` and `1` short-circuit to a cleared or filled grid.

**`Obstacle(cells)`** with the four shapes `Ltet`, `Itet`, `Stet`, `Ttet`, plus
`normalize(cells)`, `rotations(cells)` and `allOrientations(obstacles)`.
`World.py` defines the module-level `TETS`, the expanded set actually drawn from:
12 orientations (L 4, I 2, S 2, T 4).

## Behaviour worth knowing

- **`get`/`set` take `(x, y)` but index `cells[y, x]`.** Row-major storage with
  column-major arguments. Consumers that work in `(row, col)` should confine the
  translation to one adapter module rather than spreading `x`/`y` around.
- **Placement wraps around the edges.** A tetromino whose anchor lands near a
  boundary reappears on the opposite side, so it can show up as two disconnected
  fragments. The field is a torus even when the thing you build on it is not.
- **`rho` is a floor, not a target.** The loop places whole tetrominoes until
  coverage is at least `rho`, so the result slightly overshoots — 0.2004 for a
  requested 0.2 on 64×64. Tetrominoes may also overlap each other, which is why
  coverage is measured rather than counted.
- **There is no O (square) tetromino.** Deliberate: the assignment's shape set
  omits it.

## Changes made for assignment 2

Four changes, all backward compatible at the call site — `World()` with no
arguments is still a 128×128 grid driven by the global `random` module.

1. **Configurable dimensions.** `WorldGrid` and `World` take `width` and
   `height`; assignment 2 needs 64×64.
2. **Off-by-one fix in `WorldGrid.set`.** It wrote `cells[y-1, x-1]` while `get`
   read `cells[y, x]`, so a value written at one coordinate was read back at
   another. Every occupied cell was being recorded one row and one column away
   from where it was meant to go.
3. **Rotations.** Previously only one orientation of each shape could be placed,
   so every L in the field pointed the same way. `allOrientations` now expands the
   four base shapes into all 12 distinct rotations.
4. **Injectable RNG.** `World(rng=random.Random(seed))` makes generation
   reproducible. Without it the constructor falls back to the global `random`
   module, preserving the original behaviour.

**These fixes change the fields that get generated.** The figures committed for
assignment 1 (`obstacle-field-rho-*.png`) predate them and will not reproduce
byte-for-byte from `generate-figures.py` any more — the rotations alone guarantee
a different field. The densities they illustrate are unaffected.
