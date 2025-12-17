from math import sqrt
from sudoku_utils import validate_shape, coord

class SudokuBoard:
    def __init__(self, grid=None, size=9, empty_token=0):
        self.size = size
        self.box_size = int(sqrt(size))
        self.empty_token = empty_token
        self.grid = grid if grid else [[0]*size for _ in range(size)]

        if self.box_size ** 2 != size:
            raise ValueError("Size must be a perfect square (4, 9, 16)")

        validate_shape(self.grid, self.size)

    @classmethod
    def from_file(cls, path):
        from sudoku_utils import parse_text_file, parse_csv_file
        if path.endswith(".csv"):
            grid = parse_csv_file(path)
        else:
            grid = parse_text_file(path)
        return cls(grid=grid, size=len(grid))

    def row_values(self, r):
        return self.grid[r]

    def col_values(self, c):
        return [self.grid[r][c] for r in range(self.size)]

    def box_values(self, br, bc):
        vals = []
        for r in range(br*self.box_size, (br+1)*self.box_size):
            for c in range(bc*self.box_size, (bc+1)*self.box_size):
                vals.append(self.grid[r][c])
        return vals

    def find_conflicts(self):
        conflicts = []

        # Rows
        for r in range(self.size):
            seen = {}
            for c, val in enumerate(self.row_values(r)):
                if val != self.empty_token:
                    if val in seen:
                        conflicts.append((coord(r, c),
                                          f"duplicates with {coord(r, seen[val])} in row"))
                    seen[val] = c

        # Columns
        for c in range(self.size):
            seen = {}
            for r, val in enumerate(self.col_values(c)):
                if val != self.empty_token:
                    if val in seen:
                        conflicts.append((coord(r, c),
                                          f"duplicates with {coord(seen[val], c)} in column"))
                    seen[val] = r

        # Boxes
        for br in range(self.box_size):
            for bc in range(self.box_size):
                seen = {}
                for r in range(br*self.box_size, (br+1)*self.box_size):
                    for c in range(bc*self.box_size, (bc+1)*self.box_size):
                        val = self.grid[r][c]
                        if val != self.empty_token:
                            if val in seen:
                                conflicts.append((coord(r, c),
                                                  f"duplicates with {seen[val]} in box"))
                            seen[val] = coord(r, c)
        return conflicts

    def is_valid(self):
        conflicts = self.find_conflicts()
        return (len(conflicts) == 0, conflicts)

    def is_solved(self):
        for row in self.grid:
            if self.empty_token in row:
                return False
        return self.is_valid()[0]

    def pretty_print(self):
        for r in range(self.size):
            if r % self.box_size == 0 and r != 0:
                print("-" * (self.size*2))
            for c in range(self.size):
                if c % self.box_size == 0 and c != 0:
                    print("|", end=" ")
                print(self.grid[r][c] or ".", end=" ")
            print()

    def to_file(self, path, mode="w"):
        with open(path, mode) as f:
            for row in self.grid:
                f.write(" ".join(str(v or ".") for v in row) + "\n")

# sudoku_board.py
from math import sqrt
from sudoku_utils import validate_shape, coord

class SudokuBoard:
    def __init__(self, grid=None, size=9, empty_token=0):
        self.size = size
        self.box_size = int(sqrt(size))
        self.empty_token = empty_token
        self.grid = grid if grid else [[0]*size for _ in range(size)]

        if self.box_size ** 2 != size:
            raise ValueError("Size must be a perfect square (4, 9, 16)")

        validate_shape(self.grid, self.size)

    @classmethod
    def from_file(cls, path):
        from sudoku_utils import parse_text_file, parse_csv_file
        if path.endswith(".csv"):
            grid = parse_csv_file(path)
        else:
            grid = parse_text_file(path)
        return cls(grid=grid, size=len(grid))

    def row_values(self, r):
        return self.grid[r]

    def col_values(self, c):
        return [self.grid[r][c] for r in range(self.size)]

    def box_values(self, br, bc):
        vals = []
        for r in range(br*self.box_size, (br+1)*self.box_size):
            for c in range(bc*self.box_size, (bc+1)*self.box_size):
                vals.append(self.grid[r][c])
        return vals

    def find_conflicts(self):
        conflicts = []

        # Rows
        for r in range(self.size):
            seen = {}
            for c, val in enumerate(self.row_values(r)):
                if val != self.empty_token:
                    if val in seen:
                        conflicts.append((coord(r, c),
                                          f"duplicates with {coord(r, seen[val])} in row"))
                    seen[val] = c

        # Columns
        for c in range(self.size):
            seen = {}
            for r, val in enumerate(self.col_values(c)):
                if val != self.empty_token:
                    if val in seen:
                        conflicts.append((coord(r, c),
                                          f"duplicates with {coord(seen[val], c)} in column"))
                    seen[val] = r

        # Boxes
        for br in range(self.box_size):
            for bc in range(self.box_size):
                seen = {}
                for r in range(br*self.box_size, (br+1)*self.box_size):
                    for c in range(bc*self.box_size, (bc+1)*self.box_size):
                        val = self.grid[r][c]
                        if val != self.empty_token:
                            if val in seen:
                                conflicts.append((coord(r, c),
                                                  f"duplicates with {seen[val]} in box"))
                            seen[val] = coord(r, c)
        return conflicts

    def is_valid(self):
        conflicts = self.find_conflicts()
        return (len(conflicts) == 0, conflicts)

    def is_solved(self):
        for row in self.grid:
            if self.empty_token in row:
                return False
        return self.is_valid()[0]

    def pretty_print(self):
        for r in range(self.size):
            if r % self.box_size == 0 and r != 0:
                print("-" * (self.size*2))
            for c in range(self.size):
                if c % self.box_size == 0 and c != 0:
                    print("|", end=" ")
                print(self.grid[r][c] or ".", end=" ")
            print()

    def to_file(self, path, mode="w"):
        with open(path, mode) as f:
            for row in self.grid:
                f.write(" ".join(str(v or ".") for v in row) + "\n")
