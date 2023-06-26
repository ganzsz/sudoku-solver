

from typing import List


class PlayField:
    class field: 
        def __init__(self, value=-1) -> None:
            self.value = value
            self.possibilities: List[int] = []
    

    def __init__(self, knownItems:List) -> None:
        """Parameters:
        knownItems: List:(x, y, value)
        """
        self.playArea = [[PlayField.field() for i in range(9)] for j in range(9)]
        for x, y, val in knownItems:
            self.playArea[x][y].value = val

    def __repr__(self) -> str:
        result = ""
        for rowK, row in enumerate(self.playArea):
            for celK, cel in enumerate(row):
                result += str(cel.value) if cel.value > 0 else ' '
                if (celK + 1) % 3 == 0 and celK < 8: result += '|'
            result += '\n'
            if (rowK+1) % 3 == 0 and rowK < 8: result += "---+---+---\n"
        return result

    def numbersInRow(self, row:int) -> List[int]:
        return [v.value for v in self.playArea[row] if v.value > 0]

    def numbersInColumn(self, col:int) -> List[int]:
        return [r[col].value for r in self.playArea if r[col].value > 0]

    def numbersInBlock(self, row:int, col:int) -> List[int]:
        row = row - row % 3
        col = col - col % 3
        out = []
        for r in range(row, row+3):
            for c in range(col, col+3):
                if self.playArea[r][c].value > 0: out.append(self.playArea[r][c].value)
        return out
    
    def blockingNumbers(self, row:int, col:int) -> List[int]:
        return list(set(self.numbersInBlock(row, col) + self.numbersInColumn(col) + self.numbersInRow(row)))

    def possibleNumbers(self, row:int, col:int) -> List[int]:
        blockedNumbers = self.blockingNumbers(row, col)
        return [i for i in range(1, 10) if i not in blockedNumbers]

    def isFinished(self) -> bool:
        return False not in set([self.playArea[r][c].value > 0 for c in range(9) for r in range(9)])

    def updatePosibilities(self) -> None:
        for rowK, row in enumerate(self.playArea):
            def updateCel(rowK: int, celK: int, cel:PlayField.field):
                if cel.value > 0: return
                cel.possibilities = self.possibleNumbers(rowK, celK)
                if len(cel.possibilities) == 1:
                    print(rowK, celK)
                    cel.value = cel.possibilities[0]
            
            [updateCel(rowK, celK, cel) for celK, cel in enumerate(row)]


