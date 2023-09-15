from PlayField import PlayField
from debug import debug
import sudokus.nakedSingle
import sudokus.hiddenSingle

def main():
    sudoku = PlayField(sudokus.hiddenSingle.sudoku)
    print(sudoku)
    for _ in range(10):
        sudoku.updatePosibilities(_)
        debug("run", _)
        debug(sudoku)
        if sudoku.isFinished() : break
    print("******** FINISHED ********")
    print(sudoku)
if __name__ == "__main__":
    main()