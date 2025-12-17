# sudoku_main.py
from sudoku_board import SudokuBoard
from sudoku_utils import announce

@announce("Validating Sudoku board...")
def validate_board(board):
    valid, conflicts = board.is_valid()
    if valid:
        print("Result: VALID (no conflicts detected)")
    else:
        print("Result: INVALID")
        for cell, reason in conflicts:
            print(f"- {cell}: {reason}")

@announce("Checking if Sudoku is solved...")
def solved_check(board):
    print("is_solved() ->", board.is_solved())


def interactive_input(size=9):
    print("Enter Sudoku row by row (use . or 0 for empty):")
    grid = []
    for i in range(size):
        row = input(f"Row {i+1}: ").replace(" ", "")
        grid.append([int(c) if c.isdigit() else 0 for c in row])
    return grid


if __name__ == "__main__":
    print("Sudoku Validator CLI")
    print("1. Load from file")
    print("2. Enter manually")
    choice = input("Choice: ")

    if choice == "1":
        path = input("Enter file path: ")
        board = SudokuBoard.from_file(path)
    else:
        grid = interactive_input()
        board = SudokuBoard(grid=grid)

    board.pretty_print()
    validate_board(board)
    solved_check(board)
