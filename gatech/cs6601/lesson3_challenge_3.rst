Challenge: Simulated Annealing & CSP
=====================================

Simulated Annealing Calculations
---------------------------------

Given current energy, next energy, and temperature T, compute acceptance probability:

- :math:`\Delta E > 0` → always accept (P = 1)
- :math:`\Delta E < 0` → accept with probability :math:`P = e^{\Delta E / T}`

Worked examples:

1. :math:`\Delta E = 60 - 100 = -40, T = 50 \Rightarrow P = e^{-40/50}`
2. :math:`\Delta E = 120 - 200 = -80, T = 50 \Rightarrow P = e^{-80/50}`
3. :math:`\Delta E = 25 - 100 = -75, T = 150 \Rightarrow P = e^{-75/150}`
4. :math:`\Delta E = 210 - 200 = +10 \Rightarrow P = 1`
5. :math:`\Delta E = 150 - 100 = +50 \Rightarrow P = 1`
6. :math:`\Delta E = 40 - 200 = -160, T = 300 \Rightarrow P = e^{-160/300} \approx 0.58`

CSP: Sudoku-like Grid
----------------------

Variables: :math:`x_{ij}` for a 4×4 grid.

Constraints:

- **Row**: ``all_different(x11, x12, x13, x14)`` for each row
- **Column**: ``all_different(x11, x21, x31, x41)`` for each column
- **Box**: ``all_different(x11, x12, x21, x22)`` for each 2×2 box

Algorithms: **Forward Checking** + **Minimum Remaining Values (MRV)** heuristic.

CSP: Menu Selection
--------------------

Variables: appetizer {v, e}, main-course {f, p, fp}

Constraint: ``e → (f, p, fp)`` — if appetizer is eggs, main course must include fish and/or pork.
