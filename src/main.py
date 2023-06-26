from PlayField import PlayField


def main():
    sudoku = PlayField([
        (0, 0, 8),
        (0, 5, 5),
        (0, 8, 7),
        (1, 0, 7),
        (1, 3, 2),
        (1, 5, 4),
        (1, 8, 5),
        (2, 2, 5),
        (2, 5, 9),
        (2, 6, 3),
        (3, 0, 1),
        (3, 1, 7),
        (3, 2, 9),
        (3, 3, 3),
        (3, 5, 6),
        (3, 7, 2),
        (5, 1, 2),
        (5, 3, 8),
        (5, 5, 1),
        (5, 6, 6),
        (5, 7, 9),
        (5, 8, 4),
        (6, 2, 2),
        (6, 3, 4),
        (6, 6, 7),
        (7, 0, 9),
        (7, 3, 6),
        (7, 5, 7),
        (7, 8, 2),
        (8, 0, 3),
        (8, 3, 9),
        (8, 8, 1),
    ])
    print(sudoku)
    for _ in range(20):
        sudoku.updatePosibilities()
        print(sudoku)
        if sudoku.isFinished() : break

if __name__ == "__main__":
    main()