

from typing import List
from debug import debug
from pprint import pprint

class PlayField:
    class field: 
        def __init__(self, value=-1) -> None:
            self.value = value
            self.possibilities: List[int] = []
        
        def copyPossibilities(self):
            return [n for n in range(1,9) if n in self.possibilities]
    
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
    
    def celsInRow(self, row:int) -> List[field]:
        return self.playArea[row]

    def numbersInRow(self, row:int) -> List[int]:
        return [v.value for v in self.celsInRow(row) if v.value > 0]

    def celsInColumn(self, col:int) -> List[field]:
        return [r[col] for r in self.playArea]

    def numbersInColumn(self, col:int) -> List[int]:
        return [v.value for v in self.celsInColumn(col) if v.value > 0]

    def celsInBlock(self, row:int, col:int) -> List[field]:
        row = row - row % 3
        col = col - col % 3
        out = []
        for r in range(row, row+3):
            for c in range(col, col+3):
                out.append(self.playArea[r][c])
        return out

    def numbersInBlock(self, row:int, col:int) -> List[int]:
        return [v.value for v in self.celsInBlock(row, col) if v.value > 0]



    def blockingNumbers(self, row:int, col:int) -> List[int]:
        return list(set(self.numbersInBlock(row, col) + self.numbersInColumn(col) + self.numbersInRow(row)))

    def possibleNumbers(self, row:int, col:int) -> List[int]:
        blockedNumbers = self.blockingNumbers(row, col)
        return [i for i in range(1, 10) if i not in blockedNumbers]

    def isFinished(self) -> bool:
        return False not in set([self.playArea[r][c].value > 0 for c in range(9) for r in range(9)])

    def updatePosibilities(self, iteration=0) -> None:
        for rowK, row in enumerate(self.playArea):
            def updateCel(rowK: int, celK: int, cel:PlayField.field):
                if cel.value > 0: return
                debug(rowK, celK)
                cel.possibilities = self.possibleNumbers(rowK, celK)
                nakedSingle(cel)
                if cel.value > 0: return #We found the solution
                if iteration > 0: hiddenSingle(cel, row, self.celsInColumn(celK), self.celsInBlock(rowK, celK))
                if cel.value > 0: return
                singleOutDoubles(cel, row, self.celsInColumn(celK), self.celsInBlock(rowK, celK))
                print(cel.possibilities)
            
            [updateCel(rowK, celK, cel) for celK, cel in enumerate(row)]


def nakedSingle(cel:PlayField.field):
    if len(cel.possibilities) == 1:
        cel.value = cel.possibilities[0]
        debug("Naked Single", cel.value)

def hiddenSingle(cel:PlayField.field, row:List[PlayField.field], col:List[PlayField.field], block:List[PlayField.field]):
    def findPossibleNumbers(cels:List[PlayField.field]):
        return set([p for c in cels for p in c.possibilities if c != cel])
    for collection in [row, col, block]:
        possibleNumbers = findPossibleNumbers(collection)
        nakedSingle = [p for p in cel.possibilities if p not in possibleNumbers]
        if len(nakedSingle) == 1:
            cel.value = nakedSingle[0]
            debug("Hidden Single", cel.value)
            return

def singleOutDoubles(cel:PlayField.field, row:List[PlayField.field], col:List[PlayField.field], block:List[PlayField.field]):
    def hasher(cel:PlayField.field) -> str: [str(n) for n in cel.possibilities]
    def removeNumbers(l:List[int], remove:List[int]):
        for n in remove:
            try:l.remove(n)
            except: pass
    
    celHash = hasher(cel)
    for collection in [row, col, block]:
        for ccel in collection:
            if celHash == hasher(ccel):
                print("double", celHash)
                for c in collection:
                    if c is cel or c is ccel: continue
                    removeNumbers(c, ccel.possibilities)
        