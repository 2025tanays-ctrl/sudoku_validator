# sudoku_utils.py
import csv
import time

LOG_FILE = "sudoku_log.txt"

def announce(message):
    """Decorator to announce start/end of heavy operations"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(message)
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            with open(LOG_FILE, "a") as f:
                f.write(f"{message} | Time: {end-start:.4f}s\n")
            print("Operation complete.\n")
            return result
        return wrapper
    return decorator


def validate_shape(grid, size):
    if len(grid) != size:
        raise ValueError("Invalid number of rows")
    for row in grid:
        if len(row) != size:
            raise ValueError("Invalid number of columns")


def coerce_cell_value(val):
    if val in ('.', '0', 0, ''):
        return 0
    if str(val).isdigit():
        return int(val)
    raise ValueError(f"Invalid cell value: {val}")


def parse_text_file(path):
    grid = []
    with open(path) as f:
        for line in f:
            line = line.strip().replace(" ", "")
            if not line:
                continue
            grid.append([coerce_cell_value(c) for c in line])
    return grid


def parse_csv_file(path):
    grid = []
    with open(path, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            grid.append([coerce_cell_value(c) for c in row])
    return grid


coord = lambda r, c: f"R{r+1}C{c+1}"
